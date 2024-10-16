from django.test import TestCase

from ...models import Product, Stock


class StockModelTest(TestCase):
    
    def setUp(self):
        
        product_data = {
            'name': 'product_test',
            'price': 10
        }
        
        category_name = 'category_test'
        
        self.product = Product.objects.create(**product_data)
        self.product.set_category(category_name)


    '''
    Teste responsavel por verificar se os produtos estao sendo ou nao adicionados em estoque.
    Tambem verifica a funcionalidade do metodo set_quantity.
    '''
    def test_item_added_out_of_stock(self):
        stock = Stock.objects.create(
            product=self.product,
        )
        stock.set_quantity(10)
        stock.set_quantity(-5)
        
        self.assertEqual(stock.quantity, 5)
        self.assertEqual(stock.product.name, 'product_test')
    
    
    '''
    Teste responsavel por verificar o lancamento da excessao ValueError, ao tentar retirar
    itens nao presentes em estoque.
    '''
    def test_stock_is_negative(self):
        stock = Stock.objects.create(
            product=self.product,
        )
        
        with self.assertRaises(ValueError):  
            stock.set_quantity(-10)