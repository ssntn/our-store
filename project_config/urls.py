"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views.home import home
from api.views.management import check_neon_connection
from api.views.products import product

urlpatterns = [
    # Management
    path('admin/', admin.site.urls),
    path('health-check/neon/', check_neon_connection, name='health_check_neon'),
    path('health-check/', home, name='health_check'),
    path('', home, name='home'),

    # Products
    path('products/', product),
    path('products/<int:id>', product)
]
