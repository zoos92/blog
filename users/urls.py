"""Определяет схемы URL для пользователей"""

from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Страница входа
    path(r'login/', LoginView.as_view(template_name='users/login.html'), name='login'),  
    path(r'logout/', views.logout_view, name='logout'),
    path(r'register/', views.register, name='register'),
]