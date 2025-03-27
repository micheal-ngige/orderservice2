from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
