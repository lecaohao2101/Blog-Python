# tao ra cac duong day path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# luu cac duong dan path
urlpatterns = [
    path('', views.home),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    # path('login/', auth_views.login, {'template_name': 'pages/login.html'}, name='login'),
    path('login/', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),


]
