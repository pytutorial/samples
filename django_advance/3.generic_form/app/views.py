from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Product

def index(request):
    return render(request, 'index.html', {'products': Product.objects.all()})

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'product_form.html'
    success_url = reverse_lazy('home')

class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'product_form.html'
    success_url = reverse_lazy('home')

def deleteProduct(request, id):
    p = get_object_or_404(Product, pk=id)
    if p:
        p.delete()
    return redirect('home')
