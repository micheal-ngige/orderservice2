from django.db import models
from customers.models import Customer

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} - {self.amount}"
