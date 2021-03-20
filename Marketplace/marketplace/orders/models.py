from django.db import models

# Create your models here.
class Order(models.Model):
    marketplace = models.CharField(max_length=50)
    idFlux = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    order_amount = models.CharField(max_length=50)
    #order_purchase_date = models.DateField()
