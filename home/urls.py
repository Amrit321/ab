from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('allnews/',views.allnews,name='allnews')
]