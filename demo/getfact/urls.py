from . import views
from django.urls import path

urlpatterns = [
    path('getfact/',views.getfact),
    path('showfcat/',views.show_fact)
]