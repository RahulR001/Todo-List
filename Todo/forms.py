from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Todolist


class TaskForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['tasktitle', 'taskDesc', 'checked']


class NewUser(UserCreationForm):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
