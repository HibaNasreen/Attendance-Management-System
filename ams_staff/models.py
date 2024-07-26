from django.db import models
from django.contrib.auth.models import User

from ams_admin.models import Semester,Session_Year,Staff,Subject

# Create your models here.


class Student(models.Model):
    admin = models.OneToOneField(User,on_delete=models.CASCADE,related_name='staff_student_profile')
    semester_id=models.ForeignKey(Semester,on_delete=models.DO_NOTHING,blank=True,null=True)
    session_year_id=models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + ' ' + self.admin.last_name
    
class Attendance(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    is_present = models.BooleanField(default=False)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.student.admin.first_name + ' ' + self.student.admin.last_name + ' ' +self.subject.name 