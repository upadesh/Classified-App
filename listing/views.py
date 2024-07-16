from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from .models import ClassifiedAd
from company.models import Company
from .forms import ClassifiedAdForm

# Create the ADs
class ClassifiedAdCreateView(LoginRequiredMixin, CreateView):
    model = ClassifiedAd
    form_class = ClassifiedAdForm
    template_name = 'listing/submit_ads.html'
    success_url = reverse_lazy('company_dashboard')

    def dispatch(self, request, *args, **kwargs):
        # Check if the user is in the 'Company' group
        if not request.user.groups.filter(name='Company').exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

    def form_valid(self, form):
        form.instance.user = self.request.user # Link the ad to the logged-in user
        messages.success(self.request, 'Your ad has been posted successfully!')
        return super().form_valid(form)

# Detail View of the ADs
class ClassifiedAdDetailView(DetailView):
    model = ClassifiedAd
    template_name = 'listing/detail.html'
    context_object_name = 'ad'
    
# Update the ads
class ClassifiedAdUpdateView(LoginRequiredMixin, UpdateView):
    model = ClassifiedAd
    form_class = ClassifiedAdForm
    template_name = 'listing/update_ads.html'
    success_url = reverse_lazy('company_dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.company = Company.objects.get(user=self.request.user)
        messages.success(self.request, 'Ad updated successfully!')
        return super().form_valid(form)

    def test_func(self):
        ad = self.get_object()
        return ad.company.user == self.request.user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied("You do not have permission to edit this ad.")
        return super().handle_no_permission()

# Delete the listing
class ClassifiedAdDeleteView(LoginRequiredMixin, DeleteView):
    model = ClassifiedAd
    template_name = 'listing/confirm_delete.html'
    success_url = reverse_lazy('company_dashboard')

    def dispatch(self, request, *args, **kwargs):
        ad = self.get_object()
        if not request.user.groups.filter(name='Company').exists():
            raise PermissionDenied("You do not have permission to delete this ad.")
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, "Ad deleted successfully!")
        return response