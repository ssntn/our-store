
import os
from dotenv import load_dotenv
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    return Response({"status": "success", "message": "Our store / Prices is online!"})