from django.http import HttpResponse

def hello(request):                     # http://localhost:8000/hello?name=Nguyễn+Văn+An
    name = request.GET.get('name', '')
    return HttpResponse('Hello ' + name)