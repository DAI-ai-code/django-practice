from. import views
from django.urls import path

urlpatterns = [
    path('page/', views.mypage, name="home"),
    path('bye/', views.bye, name='bye'),
    path('home/', views.home, name='home')
]