from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def index(request):
    return Response({'message': 'Hello'})

@api_view(['POST'])
def createProduct(request):   
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True, 'product': serializer.data})
    else:
        return Response({'success': False, 'errors': serializer.errors})    