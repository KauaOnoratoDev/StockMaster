from django.db import models
from .Category import Category


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    '''
    Metodo responsavel por setar a categoria do produto, ele usa o nome passado no
    parametro e cria ou pega do banco de dados a categoria relacionada.
    '''
    
    def set_category(self, category_name):
        category, created = Category.objects.get_or_create(name=category_name)
        self.category = category
        
    def __str__(self) -> str:
        return self.name
        