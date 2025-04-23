from django.urls import path
from . import views


urlpatterns = [
    path('', views.terms_of_use, name='terms'),
]
