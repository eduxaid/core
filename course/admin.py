"""
Eduxa Course Admin
@author   Sandi Andrian <sandi.andrian@eduxa.id>
@since    Apr 03, 2021
"""
from django.contrib import admin

from .models import Category

admin.site.register(Category)