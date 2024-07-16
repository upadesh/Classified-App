# from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView

from .forms import UserRegistrationForm

# User Creation Form
class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        if password:
            user.set_password(password)
        user.save()
        group = Group.objects.get(name='User')
        user.groups.add(group)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid registration information. Please check all the fields")
        return super().form_invalid(form)
    

# class RegularUserView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
#     template_name = 'user_view.html'
#     permission_required = 'user.view_model'