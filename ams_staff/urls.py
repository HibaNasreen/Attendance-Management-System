from django.urls import path
from . import views

app_name = 'ams_staff'
urlpatterns = [
    
    path('staff-base/',views.staff_base,name='staff_base'),
    
    # student
    path('staff-view-students/',views.staff_view_students,name='staff_view_students'),
    path('add-student/',views.ADD_STUDENT,name='add_student'),
    
    # subjects
    path('select-subject/',views.staff_select_subject,name='staff_select_subject'),
    path('edit-subject/',views.staff_edit_subject,name='staff_edit_subject'),

    # mark attendance
    path('mark-attendance/',views.staff_mark_attendance,name='staff_mark_attendance'),

    # enter att
    path('enter-attendance/<int:id>',views.staff_enter_attendance,name='staff_enter_attendance'),

    # view attendance
    path('view-attendance/',views.staff_view_attendance,name='staff_view_attendance'),


    # report
    #path('report/',views.staff_report,name='staff_report'),
   path('report/', views.generate_attendance_report, name='attendance_report'),

    

]

