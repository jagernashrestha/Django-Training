from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField(default = 22)
    address = models.TextField()
    email = models.EmailField(unique = True)

    def __str__(self):
        return self.name

class Cars(models.Model):
    car_name = models.CharField(max_length = 100)
    speed = models.IntegerField(default = 50)

    def __str__(self):
        return self.car_name
