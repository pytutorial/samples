from django.shortcuts import render

def hello(request):     # http://localhost:8000/hello?name=Nguyễn+Văn+An
    name = request.GET.get('name', '')
    return render(request, 'index.html', {'name': name})