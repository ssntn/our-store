
from dotenv import load_dotenv
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.model.product import Product as p
from ..serializers import ProductSerializer

@api_view(['GET'])
def get(request, id):
  
  if id:
    product = get_object_or_404(p, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

  productList = p.objects.all()
  serializer = ProductSerializer(productList, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def create(request):
  pass