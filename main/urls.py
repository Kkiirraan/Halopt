
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_user,name='login'),
    path('register/', views.register_user, name='register'),
]
from django.urls import path
from . import views

urlpatterns = [
    path("login_user",views.login_user,name="login_user"),
    
]
