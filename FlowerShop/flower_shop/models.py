from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)


class ServiceFeature(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='site_media')
