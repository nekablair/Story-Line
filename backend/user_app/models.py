from django.db import models
from django.contrib.auth.models import User

# thinking of adding parents as a group with greater control over the children's accounts
# Create your models here.
class User(models.Model):
    username = models.CharField()
    email = models.EmailField()
    password = models.CharField()
    age = models.IntegerField()
    first_name = models.CharField()
    last_name = models.CharField()
    address_street_1 = models.CharField()
    address_street_2 = models.CharField(blank=True)
    city = models.CharField(max_length=2)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()