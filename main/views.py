from django.shortcuts import render,redirect

# Create your views here.
def login_user(request):
    return render(request,'main\login.html')

#User register view
def register_user(request):
    return render(request,'register.html')