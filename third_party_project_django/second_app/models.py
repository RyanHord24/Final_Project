from django.db import models
from django.core import validators as v

class Pokemon(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    level = models.IntegerField(default=1, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])
    date_encountered = models.DateField(default="2008-01-01")
    description = models.TextField(default="Unknown", validators=[v.MinLengthValidator(7), v.MaxLengthValidator(150)])
    captured = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.name}"