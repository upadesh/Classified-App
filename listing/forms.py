from django import forms
from .models import ClassifiedAd, Location, SubCategory

class ClassifiedAdForm(forms.ModelForm):
    class Meta:
        model = ClassifiedAd
        fields = ['title', 'description', 'subcategory','website', 'price', 'location','contact_email', 'contact_phone', 'images', 'status',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'id': 'id_title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'id': 'id_description'}),
            'subcategory': forms.Select(attrs={'class': 'form-control', 'id': 'id_subcategory'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website', 'id': 'id_website'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price', 'id': 'id_price'}),
            'location': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Location', 'id': 'id_location'}),            
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Contact Email', 'id': 'id_contact_email'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Phone', 'id': 'id_contact_phone'}),
            'images': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'id_images'}),
            'status': forms.Select(attrs={'class': 'form-control', 'id': 'id_status'}),
        }
