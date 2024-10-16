from django.db import models

from .Product import Product


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock')
    quantity = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    '''
    Metodo responsavel por verificar a quantidade de itens em estoque e adicionar ou
    remover produtos se a quantidade em estoque for suficiente
    '''
    
    def set_quantity(self, quantity):
        if quantity < 0 and abs(quantity) > self.quantity:
            raise ValueError('Erro ao retirar produto! Estoque insuficiente')
        
        self.quantity += quantity
    
    def __str__(self) -> str:
        return f'{self.product} - {self.quantity}'
