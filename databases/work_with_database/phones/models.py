from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)
    # TODO: Добавьте требуемые поля
    pass
