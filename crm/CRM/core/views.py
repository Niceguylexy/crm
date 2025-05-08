from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateUserRecord
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth .decorators import login_required
from .models import Record
# Create your views here.

# homepage
def index(request):
    return render(request, 'core/index.html')


#register
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'core/register.html', context=context)


# login a user
def login(request):
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')

    context = {
        'form': form
    }
    return render(request, 'core/login.html', context=context)


# dashboard
@login_required(login_url='login')
def dashboard(request):
    my_record = Record.objects.all()
    context = {
        'records': my_record
    }
    return render(request, 'core/dashboard.html', context=context)

# create user record
@login_required(login_url='login')
def create_user_record(request):
    form = CreateUserRecord()

    if request.method == 'POST':
        form = CreateUserRecord(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard')
        
    context = {
        'form': form
    }

    return render(request, 'core/create-record.html', context=context)


# user logout
def logout(request):
    auth.logout(request)

    return redirect('login')
