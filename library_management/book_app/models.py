from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=200, blank=False, null=False)
    isbn = models.CharField(max_length=200, blank=False, null=False)
    genre = models.CharField(max_length=200, blank=False, null=False)
    published_date = models.DateField(default="2015-01-1")

