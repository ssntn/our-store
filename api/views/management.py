
from dotenv import load_dotenv
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def check_neon_connection(request):
    try:
        # Try executing a simple query to check the connection
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
        
        return Response({"status": "success", "message": "Connected to NeonDB!"})
    except Exception as e:
        return Response({"status": "error", "message": f"Connection failed: {str(e)}"}, status=500)
    
    
