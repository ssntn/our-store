from django.shortcuts import render

import psycopg2
import os
from dotenv import load_dotenv
from django.http import JsonResponse

# Load environment variables
load_dotenv("neon.env")

DATABASE_URL = os.getenv("DATABASE_URL")

def check_neon_connection(request):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        return JsonResponse({"status": "success", "message": "Connected to NeonDB!"})
    except psycopg2.OperationalError as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
