
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_user,name='login'),
<<<<<<< HEAD
    path('register/', views.register_user, name='register'),
]

=======
    path('register', views.register_user, name='register'),
]
>>>>>>> 59273d9de9ba8cc7a2330e2b164b94ae6ac7ff5e
