from django.shortcuts import render,redirect

# Create your views here.
def login_user(request):
<<<<<<< HEAD
    return render(request,'main/login.html')

#User register view
def register_user(request):
    return render(request,'main/register-1.html')

=======
    return render(request,'main\\login.html')

#User register view
def register_user(request):
    return render(request,'main\\register1.html')
>>>>>>> 59273d9de9ba8cc7a2330e2b164b94ae6ac7ff5e
