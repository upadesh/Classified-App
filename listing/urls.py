from django.urls import path
from .views import ClassifiedAdCreateView, ClassifiedAdDetailView, ClassifiedAdUpdateView, ClassifiedAdDeleteView

urlpatterns = [  
    # path('', listing, name='listing'),
    path('create/', ClassifiedAdCreateView.as_view(), name='create_listing'),
    path('ad/<int:pk>/', ClassifiedAdDetailView.as_view(), name='classified_ad_detail'),
    path('ad/<int:pk>/update/', ClassifiedAdUpdateView.as_view(), name='update_listing'),
    path('ad/<int:pk>/delete/', ClassifiedAdDeleteView.as_view(), name='delete_listing'),
]