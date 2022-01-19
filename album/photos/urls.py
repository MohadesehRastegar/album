from django.urls import path
from django.views.generic.base import View
from .views import *

urlpatterns = [
    path('',gallery,name='gallery'),
    path('photo/<str:pk>/',viewPhoto,name='photo'),
    path('add/',addPhoto,name='add')
]
