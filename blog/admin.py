from django.contrib import admin
from .models import (  # . indicating directory of models (same as admin.py)
    Post,  # Importing the Post model from models.py
    Comment,  # Importing the Comment model from models.py
)
from django_summernote.admin import SummernoteModelAdmin


#  Registering a class with a decorator is more Pythonic & allows us to
#  customise how the models we are registering will appear on the admin site.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on',)
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
