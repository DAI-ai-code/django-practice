from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert),
    path('delete/', views.delete),
    path('added/', views.get_insert_details),
    path('deleted/', views.del_details),
]