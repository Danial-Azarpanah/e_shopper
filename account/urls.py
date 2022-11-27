from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('otplogin', views.OtpLoginView.as_view(), name='user_otp_login'),
    path('checkotp', views.CheckOtpView.as_view(), name='check_otp'),
    path('logout', views.logout_user, name='logout'),
]
