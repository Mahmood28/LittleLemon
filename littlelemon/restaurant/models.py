from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=255)
    booking_date = models.DateTimeField()
    no_of_guests = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name} - {self.booking_date.strftime('%d-%m-%Y %H:%M')}"
