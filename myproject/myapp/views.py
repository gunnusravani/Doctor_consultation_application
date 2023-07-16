from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from tablib import Dataset
from datetime import date 
from . models import Doctors,Blood,Appointment
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')
def doctor(request):
    a=request.GET['problem']
    if(a=='fever'):
        feature=Doctors.objects.filter(specialization='General physician')
        return render(request,'doctor.html',{'feature':feature})
    elif(a=='BP'):
        feature=Doctors.objects.filter(specialization='Cardiologist')
        return render(request,'doctor.html',{'feature':feature})
    elif(a=='Sugar'):
        feature=Doctors.objects.filter(specialization='General physician')
        return render(request,'doctor.html',{'feature':feature})
    elif(a=='stroke'):
        feature=Doctors.objects.filter(specialization='Cardiologist')
        return render(request,'doctor.html',{'feature':feature})

def appoint(request):
    return render(request,'Appoint.html')
def final(request):
    name=request.GET['name']
    age=request.GET['age']
    date=request.GET['date']
    contact=request.GET['phone']
    email=request.GET['email']
    dname=request.GET['dname']
    feature=Doctors.objects.get(name=dname)
    dic={
        "Name":name,
        "Age":age,
        "date":date,
        "contact":contact,
        "email":email
    }
    msg=f'name:{dic["Name"]}\n'
    msg=msg+f'Age:{dic["Age"]}\n'
    msg=msg+f'Contact:{dic["contact"]}\n'
    msg=msg+f'email:{dic["email"]}\n'
    b=Appointment()
    b.username=name
    b.Date_of_appointment=date
    b.Docname=dname
    b.save()
    a=feature.email
    subject="Patient details"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=recipient_list = [a, ]
    send_mail( subject, msg, email_from, recipient_list )
    return render(request,'final.html')
def doc1(request):
    feature=Doctors.objects.all()
    return render(request,'doc1.html',{'feature':feature})
def blood(request):
    feature=Blood.objects.all()
    return render(request,'blood.html',{'feature':feature})
def Book(request):
    return render(request,'Book.html')
def final1(request):
    name=request.GET['name']
    age=request.GET['age']
    date=request.GET['date']
    contact=request.GET['phone']
    email=request.GET['email']
    bgroup=request.GET['bgroup']
    units=request.GET['units']
    msg1=f'name:{name}\n'
    msg1=msg1+f'age:{age}\n'
    msg1=msg1+f'date:{date}\n'
    msg1=msg1+f'contact:{contact}\n'
    msg1=msg1+f'bgroup:{bgroup}\n'
    msg1=msg1+f'units:{units}\n'
    a=Blood.objects.get(bloodgroup=bgroup)
    b=a.email
    c=a.no_of_units_available
    c=int(c)-int(units)
    a.no_of_units_available=c
    a.save()
    subject="Patient details"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=recipient_list = [b, ]
    send_mail( subject, msg1, email_from, recipient_list )
    subject1="Conformation mail"
    receipient_list1=[email,]
    msg2="Your appointment is sent to the doctor successfully,time of appointment will be sent shortly"
    send_mail(subject1,msg2,email_from,receipient_list1)
    return render(request,'final1.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def login1(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
         
            auth.login(request,user)
          
            return redirect('final3')
        else:
            messages.info(request,'Credentials are invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
def register1(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if(password==password2):
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return  redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already used')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not the same')
            return redirect('register')
    else:
        return redirect('register')
def final3(request):
    return render(request,'final3.html')

def final2(request):
    a=request.GET['username']
    feature=Appointment.objects.filter(username=a)
    return render(request,'final2.html',{'feature':feature})

def navbar(request):
    return render(request,'navbar.html')