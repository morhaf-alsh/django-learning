from django.db import models
# Create your models here.

car_types = (

    ("light vehicle","light vehicle"),
    ("meduim vehicle","meduim vehicle"),
    ("heavy vehicle","heavy vehicle")

)



class Car(models.Model):
    request_no = models.CharField(max_length=50, default='', unique=True)
    brand = models.CharField(max_length=50)
    number = models.IntegerField(validators=[])
    car_type = models.CharField(
        max_length=50,
        choices= car_types,
        default = "light vehicle"
         )
    time_in = models.TimeField(auto_now_add=True)
    time_out = models.TimeField(auto_now=False, auto_now_add=False)
    time_reserved = models.DurationField()
    
    def __str__(self):
        return str(self.number)

    def time_reserved(self):
        return (self.time_in - self.time_out)/60
