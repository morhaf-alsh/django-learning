from django.db import models
# Create your models here.

car_types = (

    ("light vehicle","light vehicle"),
    ("meduim vehicle","meduim vehicle"),
    ("heavy vehicle","heavy vehicle")

)

class Cars(models.Model):
    
    brand = models.CharField(max_length=50)
    number = models.IntegerField(validators=[])
    car_type = models.CharField(
        max_length=50,
        choices= car_types,
        default = "light vehicle"
         )
    time_in = models.TimeField()
    time_out = models.TimeField()
    
    def __str__(self):
        return self.number

    def time_reserved(self):
        return (self.time_in - self.time_out)/60
