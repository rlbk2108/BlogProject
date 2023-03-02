import datetime

from django.db import models


class Client(models.Model):
    initials = models.CharField(max_length=50)
    balance = models.IntegerField()


class Car(models.Model):
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    mileage = models.IntegerField()
    is_rented = models.BooleanField(default=False)


class Sharing(models.Model):
    client = models.ManyToManyField(Client)
    car = models.ManyToManyField(Car)
    date_of_issue = models.DateTimeField(auto_now_add=True)
    date_of_return = models.DateTimeField()
    cost_per_day = models.IntegerField(default=100)
    number_of_days = models.IntegerField()
    final_payment = models.IntegerField(auto_created=True)

    def final_check(self):
        return self.number_of_days * self.cost_per_day
