from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        request.session['name'] = name
        return redirect('page2')

    return render(request, 'index.html')

def page2(request):
    name = request.session.get('name', '')
    return render(request, 'page2.html', {'name': name})