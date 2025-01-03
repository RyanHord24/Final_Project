from django.db import models
from django.core import validators as v
from .validators import validate_name, validate_school_email

class Student(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False, validators=[validate_name])
    student_email = models.EmailField(null = False, blank = False, validators=[validate_school_email])
    personal_email = models.EmailField(null = False, blank = False)
    dorm_number = models.IntegerField(default=1, null = False, blank = False, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])

    def __str__(self):
        return f"{self.name} {self.student_email} {self.personal_email} {self.dorm_number}"
