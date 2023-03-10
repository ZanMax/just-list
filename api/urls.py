from django.urls import path
from . import views

urlpatterns = [
    path('', views.api1, name='get_data'),
    path('2', views.api2, name='get_data2'),
]
