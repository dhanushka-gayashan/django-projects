from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from . import forms
from . import models


# Create your views here.
def signup_user(request):
    if request.method == 'GET':
        return render(request, 'todo/signup.html', {'form': UserCreationForm()})
    else:
        data = request.POST

        if data['password1'] == data['password2']:
            try:
                user = User.objects.create_user(username=data['username'], password=data['password1'])
                user.save()
                login(request, user=user)
                return redirect('current_todo_list')
            except IntegrityError:
                error = 'Username has already been taken. Please choose a new username'
                return render(request, 'todo/signup.html', {'form': UserCreationForm(), 'error': error})
        else:
            return render(request, 'todo/signup.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'todo/login.html', {'form': AuthenticationForm()})
    else:
        data = request.POST
        user = authenticate(request, username=data['username'], password=data['password'])

        if user is None:
            error = 'User or Password incorrect'
            return render(request, 'todo/login.html', {'form': AuthenticationForm(), 'error': error})
        else:
            login(request, user=user)
            return redirect('current_todo_list')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def home(request):
    return render(request, 'todo/home.html')


@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'todo/create.html', {'form': forms.TodoForm()})
    else:
        try:
            form = forms.TodoForm(request.POST)
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('current_todo_list')
        except ValueError:
            return render(request, 'todo/create.html', {'form': forms.TodoForm(), 'error': 'Bad data passed in.'})


@login_required
def current_todo_list(request):
    todo_list = models.Todo.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, 'todo/current_todo_list.html', {'todo_list': todo_list})


@login_required
def completed_todo_list(request):
    todo_list = models.Todo.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'todo/completed_todo_list.html', {'todo_list': todo_list})


@login_required
def view_todo(request, todo_pk):
    todo = get_object_or_404(models.Todo, pk=todo_pk, user=request.user)

    if request.method == 'GET':
        form = forms.TodoForm(instance=todo)
        return render(request, 'todo/view_todo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = forms.TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('current_todo_list')
        except ValueError:
            return render(request, 'todo/view_todo.html', {'todo': todo, 'form': form, 'error': 'Bad Information'})


@login_required
def complete_todo(request, todo_pk):
    todo = get_object_or_404(models.Todo, pk=todo_pk, user=request.user)

    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()
        return redirect('current_todo_list')


@login_required
def delete_todo(request, todo_pk):
    todo = get_object_or_404(models.Todo, pk=todo_pk, user=request.user)

    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.delete()
        return redirect('current_todo_list')
