from django.urls import path
from . import views

urlpatterns = [
    path('', views.compare_prices, name='compare_prices'),
]
