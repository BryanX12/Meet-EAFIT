from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Encuesta


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }


class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': '¿Qué está pasando?'}), required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['content', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['carrera', 'gusta_meet_eafit', 'seguira_usando', 'satisfaccion_carrera']
        labels = {
            'carrera': 'Que estudias? (Por ejemplo ingenieria de sistemas)',
            'gusta_meet_eafit': '¿Qué tanto te gusta Meet-EAFIT del 1 al 5?',
            'seguira_usando': '¿Cuanto crees seguir usando Meet-EAFIT del 1 al 5?',
            'satisfaccion_carrera': '¿Qué tan conforme estas con tu carrera del 1 al 5?'
        }
