from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert),
    path('delete/', views.delete),
    path('added/', views.get_insert_details),
    path('deleted/', views.del_details),
    path('update/',views.update),
    path('updated/',views.update_details),
    path('printer/', views.get_emp_details),
    path('getter/', views.post_emp_details),
    path('operator/', views.operations_operator),
]