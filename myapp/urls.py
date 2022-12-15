
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("", views.home,name="home"),
    path("about/", views.about,name="about"),
    path("dryFruits/", views.dryFruits,name="dryFruits"),
    path("riceandpulses/",views.rice_and_pulses,name="rice_and_pulses"),
    path("contact/",views.contact ,name="contact"),
    path("submitted/",views.submitted ,name="submitted"),
    path("login/",views.login ,name="login"),
    path("register/",views.register ,name="register")

   
]