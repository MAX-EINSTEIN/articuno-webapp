from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from .forms import EmailUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    return render(request, 'dashboard.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.SIGNUP_REDIRECT_URL)
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = EmailUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
