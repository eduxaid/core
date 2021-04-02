"""
Eduxa Course Admin
@author   Sandi Andrian <sandi.andrian@eduxa.id>
@since    Apr 03, 2021
"""
from django.contrib import admin

# Models
from .models import *

# Utils 
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from itertools import chain

# Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "count_courses")

    def count_courses(self, obj):
        return "0"
    count_courses.short_description = _("Courses")

admin.site.register(Category, CategoryAdmin)

# Course
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "price", "category", "enrollments", "instructors")

    def category(self, obj):
        return list(obj.categories.all())
    
    def enrollments(self, obj):
        return 0
    
    def instructors(self, obj):
        return 'N/A'

admin.site.register(Course, CourseAdmin)