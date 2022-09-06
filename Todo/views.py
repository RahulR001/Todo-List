from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todolist
from .forms import TaskForm, NewUser
from django.contrib.auth import login as loginuser, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


@login_required(login_url='/login')
def update(response, id):
    ls = Todolist.objects.get(id=id)
    form = TaskForm(response.POST or None, instance=ls)
    if response.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('viewtask')
    context = {
        'form': form
    }

    return render(response, 'update todo.html', context)


@login_required(login_url='/login')
def ToDolist(response):

    if response.method == 'POST':
        form = TaskForm(response.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.unique_user = response.user
            task.save()

            return redirect('todolist')
    else:
        form = TaskForm()

    return render(response, 'todolist.html', {'form': form})


@login_required(login_url='/login')
def viewtask(request):
    if request.user.is_authenticated:
        user = request.user
        tasks = Todolist.objects.filter(unique_user=user)

    return render(request, 'viewtask.html', {'tasks': tasks})


def delete(request, id):
    ls = Todolist.objects.get(id=id)
    ls.delete()
    return redirect('viewtask')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            loginuser(request,user)
            return redirect('todolist')
        else:
            print(form)
            messages.error(request,'Username and Password Incorrect')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html',{'form':form})


def signup(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        uname = User.objects.filter(username=username)
        if password1 == password2:
            if uname:
                messages.info(request, 'Username taken')
            elif form.is_valid():
                user = form.save()
                return redirect('todolist')
            else:
                messages.info(request, 'Password too short')
        else:
            messages.info(request, 'Password mismatch')
    else:
        form = NewUser()
    return render(request, 'registration/signup.html', {'form': form})
