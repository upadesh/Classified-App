from django.urls import path
from .views import UserRegisterView

urlpatterns = [  
    # path('', login, name='login'),
    path('register', UserRegisterView.as_view(), name='user_register'),
]