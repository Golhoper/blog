from django.contrib import admin
from django.urls import path, include
from user.url import *

urlpatterns = [
    path('', include('articles.url')),
    path('user/', include('user.url')),
]
