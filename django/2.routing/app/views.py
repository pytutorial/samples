from django.http import HttpResponse

def index(request):                         # http://localhost:8000
    return HttpResponse("Home page")
    
def hello(request):                         # http://localhost:8000/hello
    return HttpResponse("Hello")    
    
def hello2(request, name):                  # http://localhost:8000/hello/Nguyen Van An
    return HttpResponse("Hello " + name)        