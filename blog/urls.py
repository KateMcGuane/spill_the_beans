from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventsList.as_view(), name='home'),
    path("<int:event_id>/", views.event_detail, name="event_detail") 
]