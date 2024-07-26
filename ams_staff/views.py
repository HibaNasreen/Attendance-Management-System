from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from accounts.models import Profile
from ams_admin.models import Session_Year,Semester
from ams_staff.models import Student,Attendance

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ams_staff.EmailBackEnd import EmailBackEnd
from ams_admin.models import Session_Year,Semester,Subject,Staff    
#from .forms import StudentRegisterForm


def staff_base(request):
    return render(request,'staff_base.html')
    


# student

def staff_view_students(request):
    students = User.objects.all().filter(profile__role = 2)
    context = {
        'students': students
    }
    return render(request,'includes/staff_view_student.html',context)
    


def ADD_STUDENT(request):
    semester=Semester.objects.all()
    session_year=Session_Year.objects.all()
    
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        semester_id = request.POST.get('semester_id')
        session_year_id = request.POST.get('session_year_id')
       

        
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email Is Already Taken')
            return redirect('ams_staff:add_student')
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username Is Already Taken')
            return redirect('ams_staff:add_student')
        else:
            user = User(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                
            )
            user.set_password(password)
            user.save()
            user.profile.role = 2
            user.profile.is_verified = True
            user.save()
            
            semester =Semester.objects.get(id = semester_id) 
            session_year = Session_Year.objects.get(id=session_year_id)


            student = Student(
                admin = user,
                session_year_id = session_year,
                semester_id = semester,
            )
            student.save()
            messages.success(request,user.first_name + " " + user.last_name + " Is Successfully Added")
            return redirect('ams_staff:add_student')

            
    context = { 
        'semester':semester,
        'session_year':session_year,
    }
    return render(request,'includes/add_student.html',context)


# select subject
def staff_select_subject(request):
    return render(request,'includes/staff_select_subject.html')


# edit subject
def staff_edit_subject(request):
    return render(request,'includes/staff_edit_subject.html')



# mark attendance
def staff_mark_attendance(request):
    context={}
    try:
        user = request.user
        staff = Staff.objects.get(admin = user)
        subject = Subject.objects.all().filter( staff = staff )
        context = {
        'subject':subject,
        }

    except:
        print("-- No --")
    
    return render(request,'includes/staff_mark_attendance.html',context)

# enter attendance
def staff_enter_attendance(request,id):
    print(id)
    
                
    students = None    
    try:
        subject = Subject.objects.get(id = id)
        semester = subject.semester_id
        students = Student.objects.all().filter(semester_id  = semester)
    except:
        print("--ERROR--")

    context = {
        'students':students
    }

    if request.method == 'POST':
        try:
            date = request.POST.get('date')
            print(date)
            present_students = request.POST.getlist('attendees')
            print(present_students)

            staff = Staff.objects.get(admin = request.user)
            subject = Subject.objects.get(id = id)
            semester_id = subject.semester
            all_students = Student.objects.all().filter(semester_id = semester_id) 

            for st in all_students:    
                att = Attendance(
                    staff = staff,
                    subject = subject,
                    student = st,
                    is_present = False,
                    date = date
                )
                att.save()
                print(st)

                print(present_students)
                if str(st.admin_id) in present_students:
                    att.is_present = True
                    att.save()
            messages.error(request,"Success")
        except:
            messages.error(request,"ERROR")



        """ for s in present_students:
            student = Student.objects.get(admin_id = s)
            att = Attendance(
                staff = staff,
                subject = subject,
                student = student,
                is_present = True,
                date = date
            )
            att.save()

        s = present_students[0]
        student = Student.objects.get(admin_id = s)
        semester_id = student.semester_id 
        all_students = Student.objects.all().filter(semester_id = semester_id) 
        
        for st in all_students:    
            if st.admin_id not in present_students:
                 att = Attendance(
                    staff = staff,
                    subject = subject,
                    student = student,
                    is_present = False,
                    date = date
                )
                att.save() 
                print(st)
    
 """


    return render(request,'includes/staff_enter_attendance.html',context)




'''def calculate_attendance_percentage(student):
    total_classes = Attendance.objects.filter(student=student).count()
    if total_classes == 0:
        return 0
    present_classes = Attendance.objects.filter(student=student, is_present=True).count()
    attendance_percentage = (present_classes / total_classes) * 100
    return round(attendance_percentage, 2)  # Rounded to two decimal places


from django.shortcuts import render
from django.db.models import Avg

def generate_attendance_report(request):
    students = Student.objects.all()
    attendance_data = []

    for student in students:
        attendance_percentage = calculate_attendance_percentage(student)
        attendance_data.append({
            'student': student,
            'attendance_percentage': attendance_percentage
        })

    average_attendance = Attendance.objects.aggregate(average=Avg('is_present'))['average'] * 100

    context = {
        'attendance_data': attendance_data,
        'average_attendance': round(average_attendance, 2)
    }

    return render(request, 'includes/attendance_report.html', context)'''



from django.db.models import Count

def generate_attendance_report(request):
    students = Student.objects.all()

    attendance_report = []
    for student in students:
        total_days = Attendance.objects.filter(student=student).count()
        present_days = Attendance.objects.filter(student=student, is_present=True).count()

        if total_days > 0:
            percentage = (present_days / total_days) * 100
        else:
            percentage = 0

        attendance_report.append({
            'student': student,
            'percentage': percentage
        })

    return render(request, 'includes/attendance_report.html', {'attendance_report': attendance_report})


# view attendance
def staff_view_attendance(request):
    return render(request,'includes/staff_view_attendance.html')


# report
def staff_report(request):
    return render(request,'includes/staff_report.html')

