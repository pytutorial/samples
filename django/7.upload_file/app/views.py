import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'index.html')
    
@require_http_methods(["POST"])    
def upload(request):
    file = request.FILES.get('image')
    if file != None and file.name != '':
        fs = FileSystemStorage()
        filepath = os.path.join('static', file.name)
        saved_path = fs.save(filepath, file)
        return redirect('/' + saved_path)
    else:
        return HttpResponse("Cannot upload file")
        