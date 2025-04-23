from django.contrib import admin
from .models import TermsOfUse


# Register your models here.
@admin.register(TermsOfUse)
class TermsOfUseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at',)
