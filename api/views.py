
import os
from dotenv import load_dotenv
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.http import require_GET

# Load environment variables
load_dotenv("neon.env")

DATABASE_URL = os.getenv("DATABASE_URL")

@api_view(['GET'])
def check_neon_connection(request):
    try:
        # Try executing a simple query to check the connection
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
        
        return Response({"status": "success", "message": "Connected to NeonDB!"})
    except Exception as e:
        return Response({"status": "error", "message": f"Connection failed: {str(e)}"}, status=500)
    
@api_view(['GET'])
@require_GET
def home(request):
    return Response({"status": "success", "message": "Our store / Prices is online!"})