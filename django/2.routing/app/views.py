from django.shortcuts import render

def index(request):
    context = {'name' : 'world'}
    return render(request, 'index.html', context)