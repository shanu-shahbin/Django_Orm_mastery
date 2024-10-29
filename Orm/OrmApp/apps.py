# apps.py
from django.apps import AppConfig

class OrmAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OrmApp'

    def ready(self):
        import OrmApp.signals  # Import the signals module to register signal handlers
