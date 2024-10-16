from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    phone_number = models.CharField(max_length=11)
    adress = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    