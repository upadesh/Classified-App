from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView
from listing.models import ClassifiedAd
from company.models import Company

# Create your views here.
class CompanyClassifiedAdHomeListView(ListView):
    model = ClassifiedAd
    template_name = 'home/index.html'
    context_object_name = 'ads'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for ad in context['ads']:
            ad.company_name = ad.user.company.company_name
            ad.logo = ad.user.company.logo
        return context
    