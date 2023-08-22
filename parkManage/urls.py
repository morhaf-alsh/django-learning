from django.urls import path
from parkManage import views
urlpatterns = [
    path('currentlist/',views.currentList),
    path('car_info/<int:id>',views.car_info),
    path('new/', views.create),
]
