from rest_framework.decorators import api_view
from rest_framework.response import Response
import cloudinary.uploader

@api_view(['POST'])
def upload(request):
  file = request.FILES['file']
  result = cloudinary.uploader.upload(file)
  return Response(result)