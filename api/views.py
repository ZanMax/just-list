from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api1(request):
    return Response({'message': 'Hello, world!'})

@api_view(['GET'])
def api2(request):
    return Response({'message': 'Hello, world2!'})