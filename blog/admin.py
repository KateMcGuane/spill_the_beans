from django.contrib import admin
from .models import Post, Comment  # . indicating directory of models (same as admin.py); Can insert multiple models
from django_summernote.admin import SummernoteModelAdmin


#  Registering a class with a decorator is more Pythonic & allows us to 
#  customise how the models we are registering will appear on the admin site.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)