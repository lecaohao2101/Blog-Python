# tao ra cac duong day path
from django.urls import path
from . import views

# luu cac duong dan path
urlpatterns = [
    path('', views.home),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),

]
