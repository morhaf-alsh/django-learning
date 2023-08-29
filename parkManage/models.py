from django.db import models
import random
import string
# Create your models here.

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
    number = models.IntegerField(validators=[])
    car_type = models.CharField(
        max_length=50,
        choices= car_types,
        null = False
         )
    time_in = models.TimeField(auto_now_add=True)
    time_out = models.TimeField(auto_now=False, auto_now_add=False)
    time_reserved = models.DurationField()
    
    def __str__(self):
        return str(self.number)

