
from dotenv import load_dotenv
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.model.product import Product as p
from ..serializers import ProductSerializer

@api_view(['GET', 'POST'])
def product(request, id=None):

  # Get all
  if request.method == 'GET':
    
    if id is not None:
      product = get_object_or_404(p, pk=id)
      serializer = ProductSerializer(product)
      return Response(serializer.data)
    
    productList = p.objects.all()
    serializer = ProductSerializer(productList, many=True)
    return Response(serializer.data)
  
  # Create one entry
  if request.method == 'POST':
    pass
    
