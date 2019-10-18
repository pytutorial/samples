from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        fullname = request.POST.get('fullname', '')
        address = request.POST.get('address', '')
        text = f'Họ tên : {fullname}, địa chỉ : {address}'
        return HttpResponse(text)