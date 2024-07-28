from django.contrib import admin
from .models import Post  # . indicating directory of models(same as admin.py)

# Register your models here.
admin.site.register(Post)  # allows custom models to appear; import Post model