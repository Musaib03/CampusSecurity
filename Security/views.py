from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login ,logout
from django.contrib.messages import error,warning,info,success
from django.http import JsonResponse
import json
import datetime


def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('index')
    # else:
    form = CreateUserForm(request.POST or None)  # Instantiate the form with request.POST if available
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'signup.html', context)


def login(request):
    # if request.user.is_authenticated:
    #     return redirect('index')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

            # Using authenticate to get a valid user object
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')  

        else:
            messages.info(request, 'Invalid username or password')  # Displaying an error message
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
