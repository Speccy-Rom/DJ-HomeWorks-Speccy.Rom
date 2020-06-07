from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    body = models.TextField()
    lte = models.TextField()
    operating_system = models.TextField()
    cpu = models.TextField()
    memory = models.IntegerField()
    matrix_camera = models.IntegerField()
    unic_camera = models.TextField()
    object = models.Manager()

class Apple(models.Model):
    common = models.ForeignKey('Phone', on_delete=models.CASCADE)
    battery = models.IntegerField()
    object = models.Manager()

class Samsung(models.Model):
    common = models.ForeignKey('Phone', on_delete=models.CASCADE)
    dictaphone = models.TextField()
    memory_card = models.TextField()
    object = models.Manager()