from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from nlp.views import *

urlpatterns = [
    
    url(r'^', index),
]
