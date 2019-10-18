from django.http import HttpResponse

def index(request):                 # http://localhost:8000
    return HttpResponse("Hello")