from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def feed(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'social/feed.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'social/register.html', context)


def profile(request):
    return render(request, 'social/profile.html')
