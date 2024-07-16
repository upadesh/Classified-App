from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    company_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    logo = models.ImageField(upload_to='static/images/company_logos/', blank=True, null=True)
    # Add other company-specific fields here

    def __str__(self):
        return self.company_name