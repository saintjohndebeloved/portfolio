from django.urls import path

from myprojectapp import views

urlpatterns = [
    path("", views.myprojectapp, name = 'myprojectapp')
]