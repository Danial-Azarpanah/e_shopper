from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('check-otp', views.CheckOtpView.as_view(), name='check_otp'),
]