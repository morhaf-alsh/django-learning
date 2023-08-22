from django.shortcuts import render
from django.views.generic import ListView
from storeManage.models import *
# Create your views here.


class CarList(ListView):
    model = Car
    context_object_name = "objects"