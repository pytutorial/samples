from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .models import User
from .forms import MyUserCreationForm

def signup(request):
   form = MyUserCreationForm()
   
   if request.method == 'POST':
       form = MyUserCreationForm(request.POST)
       if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                                    password=request.POST['password1'])
            login(request, user)
            return redirect('home')

   return render(request, 'registration/signup.html', { 'form':  form})

def index(request):
    return render(request, 'index.html')