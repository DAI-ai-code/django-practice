from . import views
from django.urls import path

urlpatterns = [
    path("delivery/", views.delivery_update)
]