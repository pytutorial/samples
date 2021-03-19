from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product, Category
import math

def createSearchUrl(keyword, categoryId):
    categoryId = categoryId or ''
    return f'?keyword={keyword}&categoryId={categoryId}'

def index(request):
    pageSize = 5
    query_params = request.GET
    keyword = query_params.get('keyword', '')
    categoryId = query_params.get('categoryId')

    products = Product.objects.all()
    
    if keyword:
        products = products.filter(Q(name__contains=keyword) | Q(code__contains=keyword))

    if categoryId:
        products = products.filter(category__id=categoryId)

    total = len(products)
    page = query_params.get('page', '')
    page = int(page) if page.isdigit() else 1
    start = (page-1) * pageSize    
    end = min(total, start+pageSize)
    num_pages = math.ceil(total/pageSize)
    searchUrl = createSearchUrl(keyword, categoryId)
    
    products = products[start:end]

    context = {
        'categories': Category.objects.all(),
        'query_params': query_params,
        'products': products,
        'num_pages': num_pages,
        'page': page,        
        'start': start,
        'end': end,
        'total': total,
        'searchUrl': searchUrl
    }

    return render(request, 'index.html', context)
