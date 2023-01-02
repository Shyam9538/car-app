from datetime import date
from gc import get_objects
from unicodedata import name
import json
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from cars.models import Car

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    '''Returns a render on the index.html file'''
    title = "Car App"
    return render(request, "cars/index.html", {"title": title, "n": Car.objects.all()})


@csrf_exempt
def cars_api(request):
    '''This gets the request data and applies it to the get and post methods'''
    if request.method == "GET":
        print(Car)
        return JsonResponse({"cars": [car.to_dict() for car in Car.objects.all()]})
    if request.method == "POST":
        data = json.load(request)
        print(data)
        todo = data.get("payload")
        car_name = data.get("car_name")
        coupe = data.get("coupe")
        print(coupe)




        top_speed = data.get("top_speed")
        date_of_purchase = data.get("date_of_purchase")
        car = Car.objects.create(
            car_name=car_name,
            coupe=coupe,
            top_speed=top_speed,
            date_of_purchase=date_of_purchase,
        )
        print(car.coupe)
        # car.save()
        return JsonResponse({"status": data})


def delete_cars(request, car_id):
    '''This method deletes the entry of that specific object'''
    if request.method == "DELETE":
        car = get_object_or_404(Car, id=car_id)
        car.delete()
        return HttpResponse()


def update_cars(request, car_id):
    '''This method updates the data in the respective object'''
    if request.method == "PUT":
        data = json.load(request)
        todo = data.get("payload")
        car_name = data.get("car_name")
        coupe = data.get("coupe")
        if 'coupe' in data:
            coupe = True
        else:
            coupe = False
        top_speed = data.get("top_speed")
        date_of_purchase = data.get("date_of_purchase")
        car = get_object_or_404(Car, id=car_id)
        print(car)
        print(car.car_name)
        car.car_name = car_name
        print(car.car_name)
        car.coupe = coupe
        car.top_speed = top_speed
        car.date_of_purchase = date_of_purchase
        car1 = car.__class__.objects.update_or_create(
            id=car_id,
            defaults={
                "car_name": car_name,
                "coupe": coupe,
                "top_speed": top_speed,
                "date_of_purchase": date_of_purchase,
            },
        )

        print(car1.coupe)
        return JsonResponse({})
