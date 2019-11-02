from rest_framework.decorators import api_view
from rest_framework.response import Response

products = [
    {'name': 'P1', 'price': 10000},
    {'name': 'P2', 'price': 20000}
]

@api_view(['GET'])
def getProducts(request):
    return Response(products)