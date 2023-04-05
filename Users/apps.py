from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Users'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
       import Users.signals
       
