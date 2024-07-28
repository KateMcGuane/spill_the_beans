from django.contrib import admin
from .models import Post, Comment  # . indicating directory of models (same as admin.py); Can insert multiple models


# Register your models here.
admin.site.register(Post)  # allows custom models to appear; import Post model
admin.site.register(Comment)