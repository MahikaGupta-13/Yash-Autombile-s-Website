from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def regUser(request):
    if request.method=='POST':
        firstName = request.POST.get('fname')
        LastName = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('passwd')
        user = User.objects.filter(username = username)
        # select * from User where username = username;

# User = model(table) filter->> check for usename has already reg or not

        if user.exists():
            messages.error(request, "Username not available")
            return redirect('/accounts/register')
        
        user = User.objects.create(
            first_name = firstName,
            last_name = LastName,
            username = username
        )
        # user = instance of User Model

        user.set_password(password)
        user.save() # Commit changes in db
        messages.success(request, "Account Created Successfully....")

        return redirect('/accounts/register')
    return render(request,'register.html')

def logUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passwd')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username....")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password...')
            return redirect('/accounts/login')
        else:
            login(request, user)
            messages.success(request, "LOgin Success...")
            return redirect('/userHome')
        
    return render(request, 'login.html')

def logoutUsers(request):
    logout(request)
    return redirect('/accounts/login')

