from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product

def index(request):
    pageSize = 5
    keyword = request.GET.get('keyword', '')
    page = int(request.GET.get('page', 1))
    products = Product.objects.filter(Q(name__contains=keyword) | Q(code__contains=keyword))

    paginator = Paginator(products, pageSize)    
    cur_items = paginator.get_page(page)    
    offset = (page - 1) * pageSize

    context = {
        'keyword': keyword,
        'cur_items': cur_items,
        'page': page,        
        'offset': offset,
        'num_pages': paginator.num_pages,
        'total': paginator.count
    }

    return render(request, 'index.html', context)
