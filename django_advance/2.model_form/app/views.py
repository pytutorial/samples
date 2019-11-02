from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def index(request):
    return render(request, 'index.html', {'products': Product.objects.all()})

def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'product_form.html', {'form': form})

def updateProduct(request, id):
    p = get_object_or_404(Product, pk=id)
    form = ProductForm(instance=p)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'product_form.html', {'form': form})

def deleteProduct(request, id):
    p = get_object_or_404(Product, pk=id)
    if p:
        p.delete()
    return redirect('home')
