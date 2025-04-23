from django.urls import path
from . import views


urlpatterns = [
    path('', views.terms_list, name='terms_list'),
]
