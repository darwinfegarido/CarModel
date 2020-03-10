from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import View
from app.models import CarModel

# Create your views here.
class CarView(View):
    greetings = 'test'
    template = loader.get_template('index.html')
    context = {}

    def get(self, request):
        cars = CarModel.objects.all()
        return render(request, "index.html", {'cars': cars})


    def post(self, request):
        car_model = CarModel.objects
        color = request.POST.get('color')
        cars = car_model.all() if(color == '') else car_model.raw("select * from app_CarModel where color = '{}'".format(color))
        return render(request, "index.html", {'cars': cars})


def add_car(request):
    name = request.POST.get('car_name')
    color = request.POST.get('car_color')

    if(name != '' and color != ''):
        CarModel(name=name, color=color).save()

    cars = CarModel.objects.all()
    return render(request, "index.html", {'cars': cars})
