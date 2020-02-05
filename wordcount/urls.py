from os import name

from django.contrib import admin
from django.urls import path
from . import views
from django.http import HttpRequest
urlpatterns = [
    path('login/', views.login),
    path('overview/',views.overview),
    path('', views.home),
    path('wordscount/',views.count,name="count"),
    path('about/',views.about,name="about")
    #path('check/',views.check(HttpRequest,2,3))
]