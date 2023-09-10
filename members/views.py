from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User


def login_user(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print(user)
            # return redirect('home')
            return HttpResponse("login success")
            
        else:
            # messages.success(request,("There is an error in loggin in."))
            # return redirect('login_user')
                return HttpResponse("cannot login")
            
            
    else:    
      return render(request,'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("Successfully logged out "))
    return redirect('home')

@csrf_protect
def register(request):
    if request.method=="POST":
            username = request.POST["username"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            email=request.POST['email']
            if password1==password2:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                user=authenticate(username=username,password=password1)
                login(request,user)
                messages.success(request,("Succesfully Registerd"))
                return HttpResponse("success")
            else:
                return HttpResponse("Wrong password")
            
    return render(request,'authenticate/register_user.html',{})