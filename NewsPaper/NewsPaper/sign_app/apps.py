from django.apps import AppConfig


class SignAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sign_app'

    def ready(self):
        import sign_app.signals
