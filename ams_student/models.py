from django.db import models
from django.contrib.auth.models import User

from ams_admin.models import Semester,Session_Year,Staff,Subject


class Student(models.Model):
    admin = models.OneToOneField(User,on_delete=models.CASCADE, related_name='student_student_profile')
    semester_id=models.ForeignKey(Semester,on_delete=models.DO_NOTHING,blank=True,null=True, related_name='semester_students')
    session_year_id=models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING,blank=True,null=True, related_name='session_year_students')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + ' ' + self.admin.last_name
    
class Attendance(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True,related_name='staff_attendance_set')
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True,related_name='student_attendance_set')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,related_name='subject_attendance_set')
    is_present = models.BooleanField(default=False)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.student.admin.first_name + ' ' + self.student.admin.last_name + ' ' +self.subject.name 

# Create your models here.
