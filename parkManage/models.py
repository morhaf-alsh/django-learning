from django.db import models
import random
import string
from datetime import datetime
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Owner(models.Model):

    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    mobile_no = PhoneNumberField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.fname

def generate_unique_code(length, model):
    
    while True:
        code = ''.join(random.choices(string.ascii_uppercase,k=length))
        if model.objects.filter(code=code).count() == 0:
            break
    return code

car_types = (

    ("light vehicle","light vehicle"),
    ("meduim vehicle","meduim vehicle"),
    ("heavy vehicle","heavy vehicle")
    )



class Current_Car(models.Model):
    
    code = models.CharField(max_length=50, default='', unique=True)
    brand = models.CharField(max_length=50)
    number = models.IntegerField(validators=[MinValueValidator(10)])
    car_type = models.CharField(
        max_length=50,
        choices= car_types,
        null = False
         )
    time_in = models.TimeField(auto_now_add=True)
    time_out = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, default=0)

    @property
    def duration(self):
        t1 = datetime.strptime(str(self.time_in), '%H:%M:%S.%f' )
        t2 = datetime.strptime(str(self.time_out), '%H:%M:%S' )
        # delta = t2 - t1
        # return (delta.total_seconds())
        return t1 - t2
        print(type(self.time_in))

    def save(self,*args,**kwargs):
        if not self.code:
            self.code = generate_unique_code(8,Current_Car)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.time_out)

