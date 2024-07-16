# company/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from .models import Company
from .forms import CompanyRegistrationForm
from django.utils.safestring import mark_safe

class CompanyInline(admin.StackedInline):
    model = Company
    can_delete = False
    verbose_name_plural = 'company'
    fk_name = 'user'

    fields = ('company_name', 'logo', 'phone', 'logo_tag')
    readonly_fields = ('logo_tag',)
    
    def logo_tag(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width="50" height="50" />')
        return "-"

    logo_tag.short_description = 'Logo'

class CustomUserAdmin(BaseUserAdmin):
    inlines = []

    def get_inline_instances(self, request, obj=None):
        inline_instances = []
        if obj:
            if obj.groups.filter(name='Company').exists():
                inline_instances.append(CompanyInline(self.model, self.admin_site))
        return inline_instances

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
