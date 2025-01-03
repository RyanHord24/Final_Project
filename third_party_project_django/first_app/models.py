from django.db import models
from django.utils import timezone
from django.core import validators as v

class Cars(models.Model):
    make = models.CharField(max_length=200, blank=False, null=False)
    model = models.CharField(max_length=200, blank=False, null=False)
    date_released = models.DateField(default="2015-01-1")
    # date_purchased = date_captured = models.DateTimeField(default=timezone.now)
    description = models.TextField(default="A standard vehicle", validators=[v.MinLengthValidator(10), v.MaxLengthValidator(150)])
    purchased = models.BooleanField(default=False)
    passengers = models.IntegerField(default=1, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])

    def __str__(self):
        return f"{self.make} {self.model}"

    def change_purchase_status(self):
        self.purchased = not self.purchased
        self.save()

    def increase_passengers(self):
        self.passengers += 1
        self.full_clean()
        self.save()

    def decrease_passengers(self):
        self.passengers -= 1
        self.full_clean()
        self.save()
