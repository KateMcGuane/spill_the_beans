from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TermsOfUse


# Register your models here.
@admin.register(TermsOfUse)
class TermsOfUseAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_on',)
    readonly_fields = ('updated_on',)
    summernote_fields = ('content',)
