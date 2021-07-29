from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('search/', search, name="search"),
    path('detail/', detail, name="detail"),
    path('community/', community, name="community"),
    path('writef/', writef, name="writef"),
    path('map/', map, name="map"),
]