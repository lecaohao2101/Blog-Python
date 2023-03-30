from django.urls import path
from . import views

urlpatterns = [
    path('', views.listblog, name='blog'),
    path('<int:id>/', views.post, name='post'),
]