
from dotenv import load_dotenv
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.model.product import Product as p
from ..serializers import ProductSerializer

@api_view(['GET', 'POST'])
def product(request):

  # Get all
  if request.method == 'GET':
    productList = p.objects.all()
    serializer = ProductSerializer(productList, many=True)
    return Response(serializer.data)
  
  # Create one entry
  if request.method == 'POST':
    pass
    
