from django.shortcuts import render
from django.views.generic import ListView, DetailView
from storeManage.models import *
# Create your views here.


class CarList(ListView):
    model = Car
    template_name = 'list_info.html'
    context_object_name = "objects"

class seller_info(DetailView):
    model = Seller
    template_name = "seller_details.html"
    context_object_name = "objects"
    

