from django.db import models

# Create your models here.
class CarModel(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.color)
