from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # url-name= room which will always point to 'room/<str:pk>/'
    path('room/<str:pk>/', views.room, name="room"),
]
