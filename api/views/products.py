
from dotenv import load_dotenv
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.model.product import Product as p
from ..serializers import ProductSerializer

@api_view(['GET'])
def get(request, id=None, page_size=None):
  if id:
    return get_by_id(id)
  
  page_size = request.GET.get('page_size')
  if page_size:
    page = int(request.GET.get('page', 1))
    return get_paginated(int(page_size), int(page))
  
  return get_all()
 

@api_view(['POST'])
def create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

#region PRIVATES
def get_by_id(id):
  product = get_object_or_404(p, pk=id)
  serializer = ProductSerializer(product)
  return Response(serializer.data)   

def get_paginated(page_size, page):

  start = (page - 1) * page_size
  end = start + page_size

  queryset = p.objects.all()[start:end]
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