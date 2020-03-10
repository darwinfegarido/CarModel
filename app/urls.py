from django.urls import path
from app import views

urlpatterns = [
    path('', views.CarView.as_view(), name="index"),
    path('add_car', views.add_car, name="add_car"),
]
