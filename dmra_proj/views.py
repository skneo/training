from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import re  # regular epression


@login_required(login_url='/login')
def home(request):
    return render(request,'home.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username').strip().lower()
        pwd = request.POST.get('pwd')
        user = authenticate(username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Login failed! Wrong credentials')
            return render(request, 'login.html')
    full_url = request.build_absolute_uri()
    return render(request, 'login.html',{'full_url':full_url})
@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('/')
@login_required(login_url='/login')
def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        user = authenticate(username=request.user.username,
                            password=old_password)
        if user is not None:
            pwd1 = request.POST.get('pwd1')
            pwd2 = request.POST.get('pwd2')
        else:
            messages.error(request, 'Error! Old password not matched')
            return redirect('/change-password')
        if (pwd1 != pwd2):
            messages.error(request, 'Error! Both passwords not matched')
            return redirect('/change-password')
        # Check if password contains at least one lowercase letter, one uppercase letter, one special character, and one number
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+])[A-Za-z\d!@#$%^&*()\-_=+]{8,16}$', pwd1):
            messages.error(
                request, 'Error! Password does not meet requirements of at least one lowercase letter, one uppercase letter, one special character only from !@#$%^&*()-_=+, one number and minimum 8 character long')
            return redirect('/change-password')
        u = User.objects.get(username=request.user)
        u.set_password(pwd1)
        u.save()
        messages.success(request, 'password changed')
        return redirect('/')
    return render(request, 'change_password.html')