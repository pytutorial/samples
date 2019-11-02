from django.shortcuts import render, redirect

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def index(request):
    return redirect('page-1')

