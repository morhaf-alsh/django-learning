from django.urls import path
from storeManage import views
from django.db.models import as_view
urlpatterns = [
    path('list/',views.CarList.as_view, name="list" )
]