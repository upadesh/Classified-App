from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .forms import CompanyRegistrationForm, CompanyLoginForm
from .models import Company
from listing.models import ClassifiedAd

# Company Registration Form
class CompanyRegisterView(CreateView):
    model = User
    form_class = CompanyRegistrationForm
    template_name = 'company/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Save user without committing to add the password later
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        if password:
            user.set_password(password)
        user.save()

        # Create a Company instance associated with the user
        company_name = form.cleaned_data.get('company_name')
        Company.objects.create(user=user, company_name=company_name)

        # Add user to the Company group
        group = Group.objects.get(name='Company')
        user.groups.add(group)

        # Log the user in after registration
        login(self.request, user)

        messages.success(self.request, "Registration successful.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid registration information. Please check all the fields")
        return super().form_invalid(form)

# Company Login Form
class CompanyLoginView(LoginView):
    template_name = 'company/login.html'
    form_class = CompanyLoginForm
    next_page = reverse_lazy('company_dashboard')

# Company Logout Form
class CompanyLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    
class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/dashboard.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.first()  # Modify as needed
        return context

class CompanyClassifiedAdListView(LoginRequiredMixin, ListView):
    model = ClassifiedAd
    template_name = 'company/dashboard.html'
    context_object_name = 'ads'

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Company').exists():
            return ClassifiedAd.objects.filter(user=user)
        else:
            raise PermissionDenied