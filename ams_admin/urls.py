from django.urls import path
from . import views


app_name = 'ams_admin'

urlpatterns = [
    
    path('admin-base/',views.admin_base,name='admin_base'),

    # verify staff
    path('verify-staff/',views.verify_staff,name='verify_staff'),
    path('verify-staff/verify/<int:id>',views.verify_staff_verify,name="verify_staff_verify"),
    path('verify-staff/remove/<int:id>',views.verify_staff_remove,name="verify_staff_remove"),


    # view students
    path('view-students/',views.view_students,name='view_students'),

    # view attendance
    path('view-attendance/',views.view_attendance,name='view_attendance'),


    # semester
    path('view-semesters/',views.view_semesters,name='view_semesters'),
    path('semester-add/',views.semester_add,name='semester_add'),
    
    

    # session year
    path('view-session-years/',views.view_session_years,name='view_session_years'),
    path('add-session-year/',views.add_session_year,name='add_session_year'),
    path('edit-session-year/<str:id>',views.edit_session_year,name='edit_session_year'),
    path('update-session-year/',views.update_session_year,name='update_session_year'),
    path('delete-session-year/<str:id>',views.delete_session_year,name='delete_session_year'),

    
    
    # subject
    path('view-subjects/',views.view_subjects,name='view_subjects'),
    path('add-subject/',views.add_subject,name='add_subject'),
    path('edit-subject/<str:id>',views.edit_subject,name='edit_subject'),
    path('update-subject/',views.update_subject,name='update_subject'),
    path('delete-subject/<str:id>',views.delete_subject,name='delete_subject'),
    

]
