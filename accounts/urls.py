from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('driverRegister',views.driverRegister,name="driverRegister"),
    path('driverLogin',views.driverLogin,name="driverLogin"),
    path('driverview',views.driverview,name="driverview"),
    path('studentview',views.studentview,name="studentview"),
    path('notpresent',views.notpresent,name="notpresent")
]
