from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegister, name='userregister'),
    path('login/', views.UserLogin, name='userlogin'),
    path('logout/', views.UserLogout, name='userlogout'),
    path('changepassword/', views.UserPasswordChange, name='userchangepassword'),
]
