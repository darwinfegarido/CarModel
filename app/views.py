from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import View
from app.models import CarModel
from app.controller.CarController import *

# Create your views here.
class CarView(View):

    def get(self, request):
        cars = getAllCars()
        return render(request, "index.html", {'cars': cars})


    def post(self, request):
        cars = getSortedCars(request)
        return render(request, "index.html", {'cars': cars})


def add_car(request):
    cars = addCar(request)
    return render(request, "index.html", {'cars': cars})
