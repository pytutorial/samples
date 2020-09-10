from django.http import HttpResponse
    
def index(request): 
    name = request.GET.get('name', '')
    gender = request.GET.get('gender', '')
    print(f'name={name}, gender={gender}')
    return HttpResponse('Hello ' + name)
   
