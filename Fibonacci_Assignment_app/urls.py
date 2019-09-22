from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('Fibonacci_calc', views.Fibonacci_calc, name='Fibonacci_calc')
    ]