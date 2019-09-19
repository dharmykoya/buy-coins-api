from django.db import models

# Create your models here.


class Bitcoin(models.Model):
    price = models.IntegerField()

    def __str__(self):
        return self.price
