from django.urls import path
from storeManage.views import *
urlpatterns = [
    path('list/', CarList.as_view(), name="list" ),
    path('seller/<int:pk>', seller_info.as_view(), name="seller" ),
]