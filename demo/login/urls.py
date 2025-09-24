from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login_page' ),
    path('fact/', views.fact, name='fact_page' )
]