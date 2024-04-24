
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'missions.index'),
    path('create', views.create, name= 'missions.create'),
]
