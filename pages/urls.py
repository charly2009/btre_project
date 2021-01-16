#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'), # this will be a main page
    path('about', views.about, name = 'about'),
    #path('', views.index, name = 'index '),
]
