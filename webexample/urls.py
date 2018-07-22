__author__ = 'Nick Terskikh. Designed by NAT Studio'

from django.conf.urls import url
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include, path

urlpatterns = [
    # path(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
]