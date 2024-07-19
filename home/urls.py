from django.urls import path
# from .views import CompanyClassifiedAdHomeListView
from .views import home

urlpatterns = [  
    # path('', CompanyClassifiedAdHomeListView.as_view(), name='home'),
    path('', home, name='home'),
]