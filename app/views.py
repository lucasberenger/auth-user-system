from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials!')
            return redirect("/login")
    else:
        return render(request, 'login.html')

    

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken!')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered!')
                return redirect('/register')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
                user.save()
                messages.info(request, 'User registered!')
                return redirect('/login')
        else:
            messages.info(request, 'Passwords not matching!')
            return redirect('/register')
    else:
        return render(request, 'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')
        
@login_required
def userlist(request):
    users = User.objects.all
    return render(request, 'userlist.html', {"users": users})


@login_required
def changepassword(request):  
   if request.method=='POST':
       new_password1=request.POST['new_password1']
       new_password2=request.POST['new_password2']

       if new_password1==new_password2:
           user = request.user
           user.set_password(new_password1) 
           user.save()
           update_session_auth_hash(request, user)
           messages.success(request, 'Password changed successfully!')
           return redirect(reverse('changepassword'))
       else:
           messages.info(request, 'Password not matching!')  
           return redirect(reverse('changepassword'))     
   else:
    return render(request, 'changepassword.html')

# !!!!!! to-do: fix redirect reverse!!!!!