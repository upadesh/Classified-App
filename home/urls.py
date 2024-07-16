from django.urls import path
from .views import CompanyClassifiedAdHomeListView

urlpatterns = [  
    path('', CompanyClassifiedAdHomeListView.as_view(), name='home'),
]