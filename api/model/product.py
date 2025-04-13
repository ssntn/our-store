from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img_url = models.URLField(max_length=500, null=True, blank=True)
    # stock_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    # TODO: Create users table. admin tsaka users
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name
