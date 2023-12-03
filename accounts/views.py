from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    #agar form submit ho to
    if request.method == "POST":
        username  = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        cpassword = request.POST.get('cpass')
        if password != cpassword or len(password) == 0 or len(cpassword) == 0:
            messages.error(request, "Password do not match")
            return redirect('register')
        # more validation can be added here 
        #check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        # user create karo
        user = User.objects.create_user(username, email, password)
        messages.success(request, "Account create successfully")
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')
    
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        print(username, password)
        if len(username) == 0 or len(password) == 0:
            messages.error(request, "Bad Login Details")
            return redirect('login')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, "Login in successfully")
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')
        
    else:
        return render(request, 'accounts/login1.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logout out successfully")
    return redirect('login')

def profile_view(request):
    return render(request, 'accounts/profile.html')
