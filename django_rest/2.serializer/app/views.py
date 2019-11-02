from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status

from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    product = serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(data=request.data, instance=product)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    product = serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def updateProductPartial(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(data=request.data, instance=product, partial=True)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    product = serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return Response({'success': True})


