import os
from django.shortcuts import render, redirect, get_object_or_404
from social_django import settings
from .models import *
from .forms import UserRegisterForm, PostForm, CommentForm, EncuestaForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
import numpy as np


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


@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('feed')
    else:
        form = PostForm()

    return render(request, 'social/post.html', {'form': form})


def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'social/profile.html', {'user': user, 'posts': posts})


def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'sigues a {username}')
    return redirect('feed')


def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'Ya no sigues a {username}')
    return redirect('feed')


def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('feed')
    else:
        form = CommentForm()
    return render(request, 'social/post.html', {'form': form})


def encuesta(request):
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            encuesta = form.save(commit=False)
            encuesta.usuario = request.user
            encuesta.save()
            return redirect('feed')
    else:
        form = EncuestaForm()
    return render(request, 'social/encuesta.html', {'form': form})


def analitica_encuesta(request):
    respuestas = Encuesta.objects.all()

    # Obtener los datos de las respuestas
    respuestas_gusta = [encuesta.gusta_meet_eafit for encuesta in respuestas]
    respuestas_seguira_usando = [encuesta.seguira_usando for encuesta in respuestas]
    respuestas_satisfaccion_carrera = [encuesta.satisfaccion_carrera for encuesta in respuestas]

    # Generar gráfico: Gusto de Meet-EAFIT
    plt.figure(figsize=(6, 4))
    plt.hist(respuestas_gusta, bins=5, range=(1, 5), edgecolor='black')
    plt.xlabel('Gusto de Meet-EAFIT')
    plt.ylabel('Cantidad de Respuestas')
    plt.title('Encuesta: Gusto de Meet-EAFIT')
    plt.grid(True)
    figura_path_gusta = os.path.join(settings.MEDIA_ROOT, 'graficos', 'grafico_gusta.png')
    plt.savefig(figura_path_gusta)

    # Generar gráfico: Seguirá usando Meet-EAFIT
    plt.figure(figsize=(6, 4))
    plt.hist(respuestas_seguira_usando, bins=5, range=(1, 5), edgecolor='black')
    plt.xlabel('Seguirá usando Meet-EAFIT')
    plt.ylabel('Cantidad de Respuestas')
    plt.title('Encuesta: Seguirá usando Meet-EAFIT')
    plt.grid(True)
    figura_path_seguira_usando = os.path.join(settings.MEDIA_ROOT, 'graficos', 'grafico_seguira_usando.png')
    plt.savefig(figura_path_seguira_usando)

    # Generar gráfico: Satisfacción con la carrera
    plt.figure(figsize=(6, 4))
    plt.hist(respuestas_satisfaccion_carrera, bins=5, range=(1, 5), edgecolor='black')
    plt.xlabel('Satisfacción con la carrera')
    plt.ylabel('Cantidad de Respuestas')
    plt.title('Encuesta: Satisfacción con la carrera')
    plt.grid(True)
    figura_path_satisfaccion_carrera = os.path.join(settings.MEDIA_ROOT, 'graficos', 'grafico_satisfaccion_carrera.png')
    plt.savefig(figura_path_satisfaccion_carrera)


    # Pasar los gráficos a la plantilla analitica_encuesta.html
    contexto = {
        'grafico_gusta': figura_path_gusta,
        'grafico_seguira_usando': figura_path_seguira_usando,
        'grafico_satisfaccion_carrera': figura_path_satisfaccion_carrera,

    }

    return render(request, 'social/analitica_encuesta.html', contexto)

