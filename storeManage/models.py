from django.db import models

# Create your models here.

class Seller(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mobile = models.BigIntegerField()

    def __str__(self):
        return self.fname
    


class Car(models.Model):

    headline = models.CharField(max_length=250)
    brand = models.CharField(max_length=50)
    details = models.TextField(max_length=1500)
    seller_id = models.ForeignKey(Seller ,on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


