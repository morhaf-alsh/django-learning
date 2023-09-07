from django.urls import path
from parkManage import views
urlpatterns = [
    # # path('',views.currentList),
    # path('car_info/<int:id>',views.car_info),
    # # path('new/', views.create),
    # path('create/', views.CarCreate.as_view()),
    # path('list/', views.CarList.as_view()),
    path('list/',views.OwnerList.as_view()),
    path('<int:pk>/', views.OwnerDetails.as_view()),
    path('create/', views.OwnerList.as_view()),
]
