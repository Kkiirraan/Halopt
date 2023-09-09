<<<<<<< HEAD

from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_user,name='login'),
    path('register/', views.register_user, name='register'),
]
=======
from django.urls import path
from . import views

urlpatterns = [
    path("login_user",views.login_user,name="login_user"),
    
]
>>>>>>> d7dc0b3ba0b5a4946a8774b0d4afb0d8a63ec7a1
