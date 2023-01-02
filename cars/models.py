from django.db import models


# Create your models here.
class Car(models.Model):
    '''This class has methods that return the name and had fields for the model'''
    car_name = models.CharField(max_length=350)
    coupe = models.BooleanField(default=False)
    top_speed = models.IntegerField(default=0)
    date_of_purchase = models.DateField()

    def __str__(self):
        '''This method returns the car name'''
        return self.car_name

    def to_dict(self):
        '''This method has the fields for the model'''
        return {
            "car_id": self.id,
            "car_name": self.car_name,
            "coupe": self.coupe,
            "top_speed": self.top_speed,
            "date_of_purchase": self.date_of_purchase,
        }
