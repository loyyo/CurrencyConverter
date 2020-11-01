from django.db import models

# Create your models here.


class Currency(models.Model):
    currency_one = models.CharField(max_length=3)
    currency_two = models.CharField(max_length=3)
