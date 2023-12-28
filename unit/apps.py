from django.apps import AppConfig


class UnitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'unit'
    verbose_name = 'Moduł.01 - Jednostki'

    def ready(self):
        import unit.signals
