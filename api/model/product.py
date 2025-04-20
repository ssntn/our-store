from django.db import models

# TODO: Create users table. admin tsaka users
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    img_url = models.URLField(max_length=500, null=True, blank=True)
    # stock_quantity = models.PositiveIntegerField()
    
    #* CREATE OPERATIONS
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    
    #* UPDATE OPERATIONS
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(null=True, blank=True)
    
    #* DELETE OPERATION
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    # deleted_by = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name
