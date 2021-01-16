#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'listings'), # this will be a main page
    path('<int:listing_id>', views.listing, name = 'listing'),
    path('search', views.search, name = 'search'),
]
