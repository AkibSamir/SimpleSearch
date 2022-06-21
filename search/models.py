from django.db import models

# Create your models here.
class Person(models.Model):
    first = models.CharField(max_length=200, blank=True, null=True)
    last = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField()
    Country = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.first
