from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .form import LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Burada index sayfasına yönlendirme yapılıyor
    """
    context = {
        'form': form
    }
    """
    return render(request, 'users/login.html', {'form': form})


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')

    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You logged out successfully....")
    return redirect('index')




