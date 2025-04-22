from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Sets up the settings for the 'about' app.

    This class sets the default primary key field type &
    registers the app with the Django project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
