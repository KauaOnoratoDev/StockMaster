from django.test import TestCase

from ...models import Customer, Orders


class OrdersModelTest(TestCase):

    # Criando objeto customer e objeto order.
    
    def setUp(self):
        customer_data = {
            'name': 'name_test',
            'cpf': '123.123.123-12',
            'phone_number': 11123456789,
            'adress': 'street test, 123b',
            'city': 'city_test',
            'state': 'state_test',
        }
        
        self.customer = Customer.objects.create(**customer_data)
        self.order = Orders.objects.create(customer_id=self.customer, status='shipped')
    
    
    '''
    Testa o metodo responsavel por incrementar os valores passados no parametro,
    verificando se a soma esta correta e se o metodo esta funcionando.
    '''
    
    def test_set_total_amount_orders(self):
        products_values = [10, 15, 40]
        self.order.set_total_amount(products_values)
                
        self.assertEqual(self.order.total_amount, sum(products_values))
        
    
    '''
    Testa o metodo responsavel por alterar o status de pagamento do pedido,
    verifica se o novo valor é 'paid' (Pago)
    '''
    
    def test_set_payment_status_to_paid(self):
        self.order.set_paymeny_status_to_paid()
        self.assertEqual(self.order.payment_status, 'paid')
    
    
    '''
    Testa o metodo responsavel por alterar o status do pedido, se esta pendente, 
    enviado, entregue ou cancelled. Tambem testa a excecao ao digitar um valor invalido.
    '''
    
    def test_set_status(self):
        self.order.set_status('pending')
        self.assertEqual(self.order.status, 'pending')
        
        with self.assertRaises(ValueError) as context:
            self.order.set_status('invalid_value')
        
        self.assertEqual(str(context.exception), 'Valor de status invalido! ("pending", "shipped", "delivered", "cancelled")')
