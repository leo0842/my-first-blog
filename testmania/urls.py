from django.contrib import admin
from django.urls import include, path
from . import views

appname = "testmania"
urlpatterns = [
    path('grade/', views.grade, name="grade")
]
