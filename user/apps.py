from django.apps import AppConfig

class UserConfig(AppConfig):
    name = 'user'
# Create the group calling the signals file  
    def ready(self):
        import user.signals