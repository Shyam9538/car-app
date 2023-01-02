from django.urls import path

from cars.views import index, cars_api, delete_cars, update_cars

urlpatterns = [
    path("", index),
    path("api/cars/", cars_api),
    path("api/cars1/<int:car_id>/", delete_cars),
    path("api/cars2/<int:car_id>/", update_cars),
]
