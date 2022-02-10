from django.db import models


# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.TextField(max_length=200)
    balance = models.TextField(null=True, blank=True)
    percentage = models.TextField(null=True, blank=True)

