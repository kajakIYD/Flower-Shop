from django.db import models


# Create your models here.


class ServicesElement(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    image = models.CharField(max_length=200)
    order_on_website = models.IntegerField()  #TODO: Make this field distinct


class PortfolioElement(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    image = models.CharField(max_length=200)

