from django.db import models
from products.models import Product


class Outflow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_outflows')
    quantity = models.IntegerField()
    cost_price = models.DecimalField(max_digits=20, decimal_places=2) # Custo registrado durante o momento da venda
    selling_price = models.DecimalField(max_digits=20, decimal_places=2) # Preço registrado na venda
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return str(self.product)
