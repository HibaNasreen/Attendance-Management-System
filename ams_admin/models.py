from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
#from ams_staff.models import Student

# Create your models here.




class Session_Year(models.Model):
    session_start=models.CharField(max_length=100)
    session_end=models.CharField(max_length=100)

    def __str__(self):
        return self.session_start + ' To ' + self.session_end
    
class Semester(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    year = models.ForeignKey(Session_Year,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Staff(models.Model):
    admin = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username
    
class Subject(models.Model):
    name=models.CharField(max_length=100)
    semester=models.ForeignKey(Semester,on_delete=models.CASCADE,null=True)
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name
    