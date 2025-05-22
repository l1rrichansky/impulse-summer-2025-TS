from django.apps import AppConfig


class RuapiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ruapiapp'

    def ready(self):
        print("Hello world")
