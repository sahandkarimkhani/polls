from django.urls import path
from . import views

#main url patterns :)
urlpatterns = [
    path('', views.index, name='index'),
]