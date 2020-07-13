from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserSignupForm


def home(request):
    context = {'user': 'Гость'}
    if request.user.is_authenticated:
        context['user'] = str(request.user)
    return render(
        request,
        'home.html',
        context
    )


def signup(request):
    if request.method == 'POST':
        register_form = UserSignupForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect(reverse('login_view'))
    else:
        register_form = UserSignupForm()

    context = {'form': register_form}
    return render(
        request,
        'signup.html',
        context
    )


def login_view(request):
    if request.method == 'POST':
        register_form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        register_form = UserLoginForm()
    context = {'form': register_form}
    return render(
        request,
        'login.html',
        context
    )


def logout_view(request):
    logout(request)
    return redirect('home')