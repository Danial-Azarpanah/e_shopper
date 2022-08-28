from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginUserForm


class LoginUserView(View):

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('home:main')
        form = LoginUserForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginUserForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:main')
            else:
                form.add_error('phone', 'No such user')
        else:
            form.add_error('phone', 'Invalid data')

        return render(request, 'account/login.html', {'form': form})
