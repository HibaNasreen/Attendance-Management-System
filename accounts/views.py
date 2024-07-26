

from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from ams_admin.models import Session_Year,Semester,Subject,Staff

from accounts.forms import RegistrationForm
def home(request):
    return render(request,'home.html')


def login(request):
    form = LoginForm()

    # if already logged in, redirect to own home page
    
    if request.user.is_authenticated:
        user = request.user
        if user.profile.role == 0:
            return redirect('ams_admin:verify_staff')
        elif user.profile.role == 1:
            return redirect('ams_staff:staff_view_students')
        elif user.profile.role == 2:
            return redirect('ams_student:view_attendance')  
        else:
            return redirect('login')

    # POST request    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

           
            username = request.POST['username']
            print(username)
            
            password = request.POST['password']
            print(password)
            user = auth.authenticate(username=username, password=password)
             
     
            if user is not None:
                
                if user.profile.is_verified == True:
                     
                    auth.login(request,user)
                    if user.profile.role == 0:
                        return redirect('ams_admin:verify_staff')
                    if user.profile.role == 1:
                        return redirect('ams_staff:staff_view_students')
                    elif user.profile.role == 2:
                        return redirect('ams_student:view_attendance')
                    else:
                        return redirect('login')
                else:
                    messages.info(request," Not verified by admin ")
            else:
                    messages.info(request," No such user")
                    return redirect('login')
    context = {
        'form':form
    }
    return render(request,'login.html',context)


def registration(request):

    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #role = form.cleaned_data['role']
            

            if User.objects.filter(username = username).exists():
                messages.info(request," Username already exists ")
                
            elif User.objects.filter(email = email).exists():
                messages.info(request," Email taken ")  
                
            else:  
                user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.profile.role = 1

                user.save()
                staff = Staff(admin = user)
                staff.save()
                messages.info(request," Account created succesfully, Please Sign in to continue") 
                return redirect('login')
        else:
            messages.info(request,"Invalid registration") 

    context = {
        'form':form
    }
    return render(request,'registration.html',context)


def logout(request):
    auth.logout(request)
    return redirect('/') 
def about(request):
    return render(request,'about.html') 

