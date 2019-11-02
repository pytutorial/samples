from rest_framework.decorators import api_view
from rest_framework.response import Response

products = [
    {'id': 1, 'name': 'P1', 'price': 10000},
    {'id': 2, 'name': 'P2', 'price': 20000},
]

@api_view(['GET'])
def hello(request):
    name = request.query_params.get('name', 'world')
    return Response({"message" : f"Hello {name}!"})

@api_view(['GET'])
def getProducts(request):
    return Response(products)

@api_view(['POST'])
def createProduct(request):
    product = request.data
    maxid = products[-1]['id'] if len(products) > 0 else 0
    product['id'] = maxid + 1
    products.append(product)
    return Response(product)

def getProductById(id):
    for p in products:
        if p['id'] == id:
            return p

@api_view(['PUT'])
def updateProduct(request, id):
    product = getProductById(id)

    if product:
        product.update(request.data)
        return Response(product)

    return Response({'success': False, 'error': 'Product not found'})

@api_view(['DELETE'])
def deleteProduct(request, id):
    product = getProductById(id)

    if product:
        products.remove(product)
        return Response({'sucess': True})

    return Response({'success': False, 'error': 'Product not found'})


