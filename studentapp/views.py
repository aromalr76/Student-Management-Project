from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.cache import cache_control, never_cache

from studentapp.models import City, Course, Student


@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def reg_fun(request):
    return render(request, 'register.html', {'data': ''})


def regdata_fun(request):
    user_name = request.POST['tbun']
    user_email = request.POST['tbemail']
    user_password = request.POST['tbpass']

    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists(): #.exists return boolean value
        return render(request, 'register.html', {'data': 'username,email and password already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name, email=user_email, password=user_password)
        u1.save()
        return redirect('log')


def log_fun(request):
    return render(request, 'login.html', {'data': ''})


def logdata_fun(request):
    uname = request.POST['tbuname']
    upassword = request.POST['tbpwd']

    user1 = authenticate(username=uname, password=upassword)

    if user1 is not None:
        if user1.is_superuser:
            login(request, user1)
            return redirect('home')
        else:
            return render(request, 'login.html', {'data': 'user is not a superuser'})
    else:
        return render(request, 'login.html', {'data': 'Enter proper username and password'})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def home_fun(request):
    return render(request, 'home.html')

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def add_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request, 'add_students.html', {'city_data': city, 'course_data': course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def read_fun(request):
    s1 = Student()
    s1.sname = request.POST['tbname']
    s1.sage = request.POST['tbage']
    s1.sphno = request.POST['tbphno']
    s1.scity = City.objects.get(city_name=request.POST['ddlcity'])
    s1.scourse = Course.objects.get(course_name=request.POST['ddlcourse'])
    s1.save()
    return redirect('add')

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def display_fun(request):
    s1 = Student.objects.all()
    return render(request, 'display.html', {'data': s1})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    c1 = City.objects.all()
    cc1 = Course.objects.all()
    if request.method == 'POST':
        s1.sname = request.POST['tbname']
        s1.sage = request.POST['tbage']
        s1.sphno = request.POST['tbphno']
        s1.scity = City.objects.get(city_name=request.POST['ddlcity'])
        s1.scourse = Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.save()
        return redirect('display')

    return render(request, 'update.html', {'data': s1, 'city_data': c1, 'course_data': cc1})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def delete_fun(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()

    return redirect('display')

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_out_fun(request):
    logout(request)
    return redirect('log')
