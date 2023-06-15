from django.contrib import admin

# Register your models here.
from api.models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Roll', 'Name', 'City']