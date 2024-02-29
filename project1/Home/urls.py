from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='Home'),
    path('About/', views.About,name='About'),
    path('Doctor/', views.Doctor,name='Doctor'),
    path('Contact/', views.Contact,name='Contact'),


]