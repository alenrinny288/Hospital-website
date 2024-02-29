from django.contrib import admin
from .models import Departments,Doctors,Booking
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','book_date','booked_on')

class Dept(admin.ModelAdmin):
    list_display = ('dept_name','dept_description')

admin.site.register(Departments,Dept)
admin.site.register(Doctors)
admin.site.register(Booking,BookingAdmin)
