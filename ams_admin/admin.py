from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Session_Year)
admin.site.register(Semester)
admin.site.register(Staff)
admin.site.register(Subject)