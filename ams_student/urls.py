from django.urls import path
from . import views

app_name = 'ams_student'

urlpatterns = [
    path('view-attendance/',views.view_attendance,name='view_attendance'),
    path('report/',views.report,name='report'),
    
]