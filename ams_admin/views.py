from django.shortcuts import render,redirect
from accounts.models import Profile
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from ams_admin.models import Session_Year,Semester,Subject,Staff
from django.contrib import messages

@login_required
def admin_base(request):
    return render(request,'admin_base.html')


# verify staff
@login_required
def verify_staff(request):
    if request.user.profile.role == 0:
        unverified = User.objects.filter(
            profile__is_verified = False
        ).exclude(
            profile__role = 0
        ).exclude(
            profile__role = 2
        ).exclude(
            username = 'superadmin'
        )
        
        context = {
            'unverified' : unverified
        }
        return render(request,'includes/verify_staff.html',context)
    else:
        return render(request,'restricted.html')
    
@login_required
def verify_staff_verify(request,id):
    if request.user.profile.role == 0:
        staff = User.objects.get(pk = id)
        
        staff.profile.is_verified = True
        staff.save()

        return redirect('ams_admin:verify_staff')
    else:
        return render(request,'restricted.html')
    
@login_required
def verify_staff_remove(request,id):
    if request.user.profile.role == 0:
        staff = User.objects.get(pk = id)
        staff.delete()
        return redirect('ams_admin:verify_staff')
    else:
        return render(request,'restricted.html')



# view student
def view_students(request):
    students = User.objects.all().filter(profile__role = 2)
    context = {
        'students': students
    }
    return render(request,'includes/view_student.html',context)



# view attendance
def view_attendance(request):
    return render(request,'includes/view_attendance.html')


# semester
def view_semesters(request):
    return render(request,'includes/view_semesters.html')

def semester_add(request):

    return render(request,'includes/semester_add.html')



# session year
def view_session_years(request):
    session=Session_Year.objects.all()

    context ={
        'session':session
    }
    return render(request,'includes/view_session_years.html',context)

def add_session_year(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year (
            session_start = session_year_start ,
            session_end = session_year_end
        )
        session.save()
        messages.success(request,'Session Are Successfully Created')
        return redirect('ams_admin:add_session_year')

    return render(request,'includes/add_session_year.html')

def edit_session_year(request,id):
    session=Session_Year.objects.filter(id=id)

    context ={
        'session':session
    }

    return render (request,'includes/edit_session_year.html',context)

def update_session_year(request):
    if request.method == "POST": 
        session_id =request.POST.get('session_id')
        session_year_start =request.POST.get('session_year_start')
        session_year_end =request.POST.get('session_year_end')

        session = Session_Year(
            id = session_id,
            session_start =session_year_start,
            session_end =session_year_end,
        )
        session.save()
        messages.success(request,'Session Are Successfully Updated !')
        return redirect('ams_admin:view_session_years')
    
def delete_session_year(request,id):
    session = Session_Year.objects.filter(id = id)
    session.delete()
    messages.success(request,'Session Are Successfully Deleted !')
    return redirect('ams_admin:view_session_years')   

    



# subjects
def view_subjects(request):
    subject = Subject.objects.all()
    
    context = {
        'subject':subject,
        
    }
    return render(request,'includes/view_subjects.html',context)

def add_subject(request):
    semester = Semester.objects.all()
    staffs = User.objects.all().filter(profile__role = 1)
    
    if request.method == "POST":
        subject_name = request.POST.get( 'subject_name')
        semester_id= request.POST.get('semester_id')
        staff_id = request.POST.get('staff_id')

        semester=Semester.objects.get(id=semester_id)
        staff = None
        #try:
        user = User.objects.get(pk = staff_id)
        staff = Staff.objects.get(admin = user)
        #except:
        #    print("Staff Does not exist")
        subject = Subject (
            name = subject_name,
            semester = semester,
            staff = staff,
        )       
        subject.save()
        messages.success(request,'Subjects are successfully added !')
        return redirect('ams_admin:add_subject')
    
    context = {
        'semester':semester,
        'staffs' :staffs,
    }

    return render(request,'includes/add_subject.html',context)

def edit_subject(request,id):
    subject=Subject.objects.get(id=id)
    semester=Semester.objects.all()
    staffs = User.objects.all().filter(profile__role = 1)
    

    context = {
        'subject':subject,
        'semester':semester,
        'staffs':staffs,
    }

    return render(request,'includes/edit_subject.html',context)

def update_subject(request):
    

    if request.method == "POST":
        subject_id=request.POST.get('subject_id')
        semester_id=request.POST.get('semester_id')
        subject_name=request.POST.get('subject_name')
        staff_id=request.POST.get('staff_id')

        semester=Semester.objects.get(id = semester_id)
        staff=Staff.objects.get(staff_id = staff_id)
        subject=Subject(
            id=subject_id,
            name=subject_name,
            semester=semester,
            staff=staff,
        )
        subject.save()
        messages.success(request,'Subject are successfully Updated')
        return redirect('ams_admin:view_subjects')
    return render(request,'includes/edit_subject.html')

def delete_subject(request,id):
    subject=Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request,'Subject are successfully Deleted')
    return redirect('ams_admin:view_subjects')


def semester_add(request):
    if request.method == "POST":
        semester_name=request.POST.get('semester_name')

        semester= Semester (
            name=semester_name,
        )
        semester.save()
        messages.success(request,'Semester are successfully Created')
        return redirect('ams_admin:semester_add')
    
    return render(request,'includes/semester_add.html')

def view_semesters(request):
    semester=Semester.objects.all()
    context= {
        'semester':semester,
    }
    
    
    return render(request,'includes/view_semesters.html',context)





    









