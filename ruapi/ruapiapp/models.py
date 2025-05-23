from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    email_address = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=80)


