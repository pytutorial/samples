from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
from .models import *

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
        
    @action(detail=True, methods=['get'])
    def get_price(self, request, pk):
        p = Product.objects.get(pk=pk)
        return Response({'price': p.price})

    @action(detail=False, methods=['get'])
    def search(self, request):
        keyword = request.GET.get('keyword', '')
        productList = Product.objects.filter(name__contains=keyword)
        data = ProductSerializer(productList, many=True).data
        return Response(data)


