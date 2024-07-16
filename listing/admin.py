from django.contrib import admin
from .models import Category, SubCategory, Location, ClassifiedAd

# Register your models here.

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category")

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Location)
admin.site.register(ClassifiedAd)