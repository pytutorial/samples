from django.shortcuts import render, redirect
from . import db
from .forms import ProductForm

def index(request):
    return render(request, 'index.html', {'products': db.products})

def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            db.addProduct(form)
            return redirect('home')

    return render(request, 'product_form.html', {'form': form})

def updateProduct(request, id):
    p = db.getProductById(id)
    form = ProductForm(initial=p)

    if request.method == 'POST':
        form = ProductForm(request.POST, initial=p)
        if form.is_valid():
            db.updateProduct(id, form)
            return redirect('home')

    return render(request, 'product_form.html', {'form': form})

def deleteProduct(request, id):
    db.deleteProduct(id)    
    return redirect('home')
