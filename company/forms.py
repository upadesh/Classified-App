from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Company


#Company New User Registration Form

class CompanyRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}))
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company Name'}))
    logo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            company = Company(user=user, company_name=self.cleaned_data['company_name'], phone=self.cleaned_data['phone'], logo=self.cleaned_data['logo'])
            company.save()
        return user





# class CompanyRegistrationForm(UserCreationForm):
#     company_name = forms.CharField(max_length=255, required=True)
#     email = forms.EmailField(required=True)
#     phone = forms.IntegerField(required=True)
#     class Meta:
#         model = User
#         fields = ["company_name", "username", "email", "phone", "password1", "password2"]

#     def __init__(self, *args, **kwargs):
#         super(CompanyRegistrationForm, self).__init__(*args, **kwargs)
#         self.fields['company_name'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Enter Company Name'
#         })
#         self.fields['username'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Enter Username'
#         })
#         self.fields['email'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Enter Email ID'
#         })
#         self.fields['phone'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Enter Phone Number'
#         })
#         self.fields['password1'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Enter Password'
#         })
#         self.fields['password2'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Confirm Password'
#         })

# Company Login Class
class CompanyLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'id_username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'id_password'}))
