from django.contrib.auth import authenticate, login
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from random import randint

from decouple import config
from uuid import uuid4
import ghasedakpack

from .forms import LoginForm, OtpLoginForm, CheckOtpForm
from .models import Otp, User

SMS = ghasedakpack.Ghasedak(config("SMS_API_KEY"))


class LoginUser(View):
    """
    View to user login panel
    """

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('home:main')
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:main')
            else:
                form.add_error('username', 'Invalid user')
        else:
            form.add_error('username', 'Invalid data')

        return render(request, 'account/login.html', context={'form': form})


class OtpLoginView(View):
    """
    View for Registering new Users by phone number
    and activating with random OTP code
    """

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect("home:main")
        form = OtpLoginForm()
        return render(request, "account/otp_login.html", {"form": form})

    def post(self, request):
        form = OtpLoginForm(request.POST)

        if form.is_valid():
            randcode = randint(1000, 9999)
            cd = form.cleaned_data
            # Send otp code to user
            # SMS.verification({'receptor': cd.get("phone"), 'type': '1', 'template': 'randcode', 'param1': randcode})
            # Token for registration with phone number. (display otp token instead of phone number for more safety)
            token = str(uuid4())
            Otp.objects.create(phone=cd["phone"], code=randcode, token=token)
            print(randcode)
            # Get the token in CheckOtp view
            return redirect(reverse("account:check_otp") + f"?token={token}")
        else:
            form.add_error("phone", "Invalid data")

        return render(request, "account/otp_login.html", {"form": form})


class CheckOtpView(View):
    """
    View for checking if the code entered by user
    is the same as the one sent
    """

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect("home:main")
        form = CheckOtpForm()
        return render(request, "account/check_otp.html", {"form": form})

    def post(self, request):
        token = request.GET.get("token")
        form = CheckOtpForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd["code"], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                login(request, user)
                otp.delete()
                return redirect("home:main")
        else:
            form.add_error("username", "Invalid data")

        return render(request, "account/check_otp.html", {"form": form})
