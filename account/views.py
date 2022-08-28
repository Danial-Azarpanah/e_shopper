from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginForm


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
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:main')
            else:
                form.add_error('phone', 'Invalid user')
        else:
            form.add_error('phone', 'Invalid data')

        return render(request, 'account/login.html', context={'form': form})
