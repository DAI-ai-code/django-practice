from . import views
from django.urls import path

urlpatterns = [
    path("loginpage/", views.login_page)
]
