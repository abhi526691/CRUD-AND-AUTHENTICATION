from django.db import models
from django.db.models.aggregates import Max
from django.db.models.enums import Choices

# Create your models here.
genderChoice = ((1, "Male"), (2, "Female"), (3, "Prefer Not To Say"))

class Profile(models.Model):
    Img = models.ImageField(upload_to='images/', default="")
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    Age = models.IntegerField()
    Gender = models.IntegerField(choices=genderChoice, blank=True)
    Desc = models.TextField(blank=True)

    def __str__(self):
        return self.firstName + " " + self.lastName
