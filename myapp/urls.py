from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path("", views.index , name = 'index.html'),
    path("index.html", views.index , name = 'index.html'),
    path("cars", views.cars , name = 'cars.html'),
    path("contact.html", views.contact , name = 'contact.html'),
    path("about.html", views.about , name = 'about.html'),
    path("terms.html", views.terms , name = 'terms.html'),
    path("faq.html", views.faq , name = 'faq.html')
]
