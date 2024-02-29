from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='Home'),
    path('About/', views.About,name='About'),
    path('Bookings/', views.Bookings,name='Bookings'),
    path('Bookings2/',views.Bookings2,name='Bookings2'),
    path('Contact/', views.Contact,name='Contact'),

]