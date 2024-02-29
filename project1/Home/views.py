from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm

# Create your views here.
def index(request):
    dict_dept ={
        'dept': Departments.objects.all()
    }
    return render(request,'index.html',dict_dept)
def About(request):
    numbers={
        'num1': [1,2,3,4,5,6,7,8,9,0]
    }
    return render(request,'about.html',numbers)
def Bookings(request):
   dict_doc={
        'doc': Doctors.objects.all()
    } 
def Bookings2(request):
   dict_doc={
        'doc': Doctors.objects.all()
    } 
   return render(request,'Bookings.html',dict_doc)
def Contact(request):
    return render(request,'contact.html')
