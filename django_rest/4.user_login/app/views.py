from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

products = [
    {'name': 'P1', 'price': 10000},
    {'name': 'P2', 'price': 20000},
]

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getProducts(request):
    return Response(products)

@api_view(['POST'])
def createUser(request):
    username = request.data.get('username', '')
    password = request.data.get('password', '')

    errors = []
    if username == '':
        errors.append('Username required')

    if User.objects.filter(username=username):
        errors.append('Username already existed')
    
    if len(password) < 6:
        errors.append('Password too short')
    
    if len(errors) == 0:
        user = User.objects.create_user(username=username, password=password)
        return Response({'success' : True})
    
    return Response({'success' : False, 'errors': errors})