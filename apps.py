# apps.py
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'heart_attack_app'

    def ready(self):
        import heart_attack_app.signals

