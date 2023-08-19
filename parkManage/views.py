from django.shortcuts import render
from parkManage.models import Car
# Create your views here.

def currentList(request):
    data = Car.objects.all().order_by('brand')
    context = {
        'data' : data
    }
    return render(request, 'list.html', context)

def car_info(request,brand):
    data = Car.objects.filter(brand=brand)
    context = {
        'data' : data
    }
    return render(request, 'list.html', context)