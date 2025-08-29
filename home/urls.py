from django.contrib import admin
from django.urls import path
# from.views import about
# from.views import home_view
from.import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('about/',views.about,name='about')
]