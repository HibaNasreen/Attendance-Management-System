from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from accounts.models import Profile


'''def view_attendance(request):
    return render(request,'includes/student_view_attendance.html')'''


from django.shortcuts import render
from .models import Student, Attendance

def view_attendance(request):
   # user=request.user
    try:
        student = Student.objects.get(admin=request.user)
        attendance_records = Attendance.objects.filter(student=student)
    except Student.DoesNotExist:
        attendance_records = []

    context = {
        'attendance_records': attendance_records,
    }

    return render(request, 'includes/view_attendance.html', context)

def report(request):
    return render(request,'includes/report.html')

