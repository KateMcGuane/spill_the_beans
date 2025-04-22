from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Sets up the settings for the 'blog' app.

    This class sets the default primary key field type &
    registers the app with the Django project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
