from django.shortcuts import render,HttpResponse,redirect
from leaveApp import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from leaveApp.models import Employees

def userlogin(request):
    if request.POST:
        username = request.POST['userid']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            user_details = User.objects.get(id=user.pk)
            employee = Employees.objects.get(userid=username)
            designation = employee.designation
        return render(request, 'leaveApp/apply.html', context={'user':user, 'designation':designation})
    return render(request,'management/login.html')

def signup(request):
    if request.POST:
        userid = request.POST['ID']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        designation = request.POST['designation']
        location = request.POST['location']
        address = request.POST['address']
        experience = request.POST['experience']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        employees = Employees.objects.create(
            userid=userid,
            name = name,
            email = email,
            mobile = mobile,
            designation = designation,
            location = location,
            address = address,
            yearsOfExperience = experience,
            password = password
        )

        if password != confirmpassword:
            return render(request, 'signup.html', context={'error_password': 'Passwords do not match :('})
        
        if User.objects.filter(username=userid).exists():
            return render(request, 'signup.html', context={'error_id': 'ID already exists'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', context={'error_email': 'Email already exists'})
        
        user = User.objects.create_user(username=userid, email=email, password=password)
        user.first_name = name
        user.save()

        return redirect('login')
    return render(request, 'management/signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')