from app.models import CarModel

def addCar(request):
    name = request.POST.get('car_name')
    color = request.POST.get('car_color')

    if(name != '' and color != ''):
        CarModel(name=name, color=color).save()

    cars = CarModel.objects.all()
    return cars

def getAllCars():
    return CarModel.objects.all()

def getSortedCars(request):
    car_model = CarModel.objects
    color = request.POST.get('color')
    cars = car_model.all() if(color == '') else car_model.raw("select * from app_CarModel where color = '{}'".format(color))
    return cars
