from django.apps import AppConfig


class TermsConfig(AppConfig):
    """
    Sets up the settings for the 'terms' app.

    This class sets the default primary key field type &
    registers
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'terms'
