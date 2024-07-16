from django.urls import path
from .views import CompanyRegisterView, CompanyLoginView, CompanyLogoutView, CompanyClassifiedAdListView

urlpatterns = [  
    # path('', views.company, name='company')
    path('register', CompanyRegisterView.as_view(), name='company_register'),
    path('login/', CompanyLoginView.as_view(), name='company_login'),
    path('logout/', CompanyLogoutView.as_view(), name='company_logout'),
    path('dashboard/', CompanyClassifiedAdListView.as_view(), name='company_dashboard'),
]