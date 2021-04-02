"""
Eduxa Course URLs
@author     Sandi Andrian <sandi.andrian@eduxa.id>
@since      Apr 03, 2021
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]