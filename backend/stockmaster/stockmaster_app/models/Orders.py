from django.db import models

from .Customer import Customer


class Orders(models.Model):
    
    # Unicas opcoes aceitas nos campos de status e payment_status 
    
    STATUS_CHOICES = (
        ('pending', 'PENDING'),
        ('shipped', 'SHIPPED'),
        ('delivered', 'DELIVERED'),
        ('cancelled', 'CANCELLED')
    )
    
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'PAID'),
        ('unpaid', 'UNPAID')
    )
    
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending')
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS_CHOICES, default='unpaid')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    '''
    Metodos responsaveis por:
    
    1 - Incrementar o valor total do pedido com base no valor passado no metodo, seja um numero, uma tupla ou uma lista.
    
    2 - Setar o status de pagamento para paid (Pago).
    
    3 - Setar o status do pedido, com uma verificacao do valor do parametro.
    '''
    
    def set_total_amount(self, value):
        if isinstance(value, (list, tuple)):
            self.total_amount += sum(value)
        
        else:
            self.total_amount += value
        
    def set_paymeny_status_to_paid(self):
        self.payment_status = 'paid'
        
    def set_status(self, status):
        valid_status = ('pending', 'shipped', 'delivered', 'cancelled')
        if not status in valid_status:
            raise ValueError('Valor de status invalido! ("pending", "shipped", "delivered", "cancelled")')
            
        self.status = status
        

    
    def __str__(self) -> str:
        return f'{self.customer_id.name} Order'