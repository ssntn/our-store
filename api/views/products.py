
from dotenv import load_dotenv
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.model.product import Product as p
from ..serializers import ProductSerializer
from ..utils import log_local as _log
 
#* Handlers
@api_view(['GET', 'POST'])
def handler(request):
  if request.method == 'GET':
    _request = request.GET
    return get(_request.get('page_size'), _request.get('page'))
  elif request.method == 'POST':
    return create(request.data)
  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)  
    
@api_view(['DELETE', 'PUT', 'GET'])
def handle_id(request, id):
  if request.method == 'GET':
    return get_by_id(id)
  elif request.method == 'DELETE':
    return delete(id)
  elif request.method == 'PUT':
    return update(request.data, id)
  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
 
def create(data):
  serializer = ProductSerializer(data=data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  print(data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get(page_size = None, page = None):
    if page_size:
        page_size = int(page_size)
        page = int(page)
        
        start = (page - 1) * page_size
        end = start + page_size
        queryset = p.objects.filter(is_deleted=False)[start:end]
    else:
        queryset = p.objects.filter(is_deleted=False)

    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

def get_by_id(id):
    try:
        product = p.objects.get(pk=id, is_deleted=False) 
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except p.DoesNotExist:
        return Response({'detail': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

def delete(id):
  try:
    product = p.objects.get(pk=id, is_deleted=False)
    product.is_deleted = True
    product.save()
    return Response({"detail": "Product deleted."}, status=status.HTTP_204_NO_CONTENT)
  except p.DoesNotExist:
    return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

def update(data, id):
    try:
        product = p.objects.get(pk=id, is_deleted=False)
    except p.DoesNotExist:
        return Response({'detail': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
