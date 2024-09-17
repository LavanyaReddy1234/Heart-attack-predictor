# urls.py
from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('', views.predict_heart_attack, name='predict_heart_attack'),
    path('login_history/', views.login_history, name='login_history'),
]
