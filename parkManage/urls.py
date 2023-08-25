from django.urls import path
from parkManage import views
urlpatterns = [
    path('',views.currentList),
    path('car_info/<int:id>',views.car_info),
    path('new/', views.create),
]
