
from dotenv import load_dotenv
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.model.product import Product as p
from ..serializers import ProductSerializer

@api_view(['GET', 'POST', 'DELETE'])
def get(request, id=None, page_size=None):
  
  # Non get methods
  if request.method == 'POST':
    return create(request)
  elif request.method == 'DELETE':
     return delete(id)

  # Get
  if id:
    return get_by_id(id)
  
  page_size = request.GET.get('page_size')
  if page_size:
    page = int(request.GET.get('page', 1))
    return get_paginated(int(page_size), int(page))
  
  return get_all()
 
def create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    print(request.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(id):
    try:
        product = p.objects.get(pk=id, is_deleted=False)
        product.is_deleted = True
        product.save()
        return Response({"detail": "Product deleted."}, status=status.HTTP_204_NO_CONTENT)
    except p.DoesNotExist:
        return Response({"detail": "Product not found."}, status=status.HTTP_400_BAD_REQUEST)


#region PRIVATES
def get_by_id(id):
  product = get_object_or_404(p, pk=id)
  serializer = ProductSerializer(product)
  return Response(serializer.data)   

def get_paginated(page_size, page):

  start = (page - 1) * page_size
  end = start + page_size

  queryset = p.objects.filter(is_deleted=False)[start:end]
  serializer = ProductSerializer(queryset, many=True)

  return Response({
      'page': page,
      'page_size': page_size,
      'results': serializer.data
  })

def get_all():
  productList = p.objects.all()
  serializer = ProductSerializer(productList, many=True)
  return Response(serializer.data)
#endregion 