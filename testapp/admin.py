from django.contrib import admin

# Register your models here.
from .models import *
#admin.site.register(Student)
admin.site.register(Class)

from django.contrib import admin
from .models import Student


def activate_students(modeladmin, request, queryset):
    # Activate selected students
    queryset.update(is_active=True)

activate_students.short_description = "Activate selected students"

def deactivate_students(modeladmin, request, queryset):
    # Deactivate selected students
    queryset.update(is_active=False)

deactivate_students.short_description = "Deactivate selected students"

@admin.register(Student)  # Register the Student2 model
class StudentAdmin(admin.ModelAdmin):
    list_display = ('phone', 'is_active')  # Add 'is_active' to the list display
    actions = [activate_students, deactivate_students]
    
#admin.site.register(Student2)    
from django.contrib import admin
from .models import Student2  # Import the Student2 model

def activate_students(modeladmin, request, queryset):
    # Activate selected students
    queryset.update(is_active=True)

activate_students.short_description = "Activate selected students"

def deactivate_students(modeladmin, request, queryset):
    # Deactivate selected students
    queryset.update(is_active=False)

deactivate_students.short_description = "Deactivate selected students"

@admin.register(Student2)  # Register the Student2 model
class Student2Admin(admin.ModelAdmin):
    list_display = ('name', 'class_name', 'is_active')  # Add 'is_active' to the list display
    actions = [activate_students, deactivate_students]  # Register the custom admin actions
