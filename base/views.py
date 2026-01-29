from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import PredictionForm

from .ml_models import MODEL_BASIC, MODEL_ADVANCED
import numpy as np

# Create your views here.

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    
        else:
            messages.error(request, 'Username OR password does not exist')
    
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
    
        else:
            messages.error(request, 'An error occured during registration...')
    
    context = {'form': form}
    return render(request, 'base/login_register.html', context)

def predict(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = list(form.cleaned_data.values())
            x = np.array([data])

            pred1 = MODEL_BASIC.predict(x)[0][0]
            pred2 = MODEL_ADVANCED.predict(x)[0][0]

            context = {"pred1": pred1, "pred2": pred2}
            return render(request, 'base/predict_result.html', context)
    else:
        form = PredictionForm()

    return render(request, "base/predict_form.html", {"form": form})
    
