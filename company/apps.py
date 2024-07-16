from django.apps import AppConfig

class CompanyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'company'
# Create the group calling the signals file  
    def ready(self):
            import company.signals