from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



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
