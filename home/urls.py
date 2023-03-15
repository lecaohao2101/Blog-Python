# tao ra cac duong day path
from django.urls import path
from . import views

# luu cac duong dan path
urlpatterns = [
    path('', views.index),
    # path('information', views.infomation),
    path('contact/', views.contact),
    path('blog/', views.blog)

]
