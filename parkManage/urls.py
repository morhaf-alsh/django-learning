from django.contrib import admin
from django.urls import path
from parkManage import views
urlpatterns = [
    path('currentlist/',views.currentList),
    path('car_info/<int:id>',views.currentList)
]
