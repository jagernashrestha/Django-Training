from django.db import models
# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length = 100)
    ingredients = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageFiels(upload_to = "recipie")

    def __str__(self):
        return self.name