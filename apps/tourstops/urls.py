from django.contrib import admin
from django.urls import path, include # new

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
]