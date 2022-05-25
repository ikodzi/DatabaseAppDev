from django.shortcuts import render, redirect
from .forms import callBackForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def index(request):
    type = ''
    return render(request, 'shop/example.html', {'type': type})


def create(request):
    error = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            error = 'Form was incorrect'
    form = UserCreationForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'registration/create.html', data)


def store(request):
    return render(request, 'main/storesinkz.html')


def call(request):
    error = ''
    if request.method == 'POST':
        form = callBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Form was incorrect'
    form = callBackForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/contact.html', data)
