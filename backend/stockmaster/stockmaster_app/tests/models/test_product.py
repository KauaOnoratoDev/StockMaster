from django.test import TestCase

from ...models import Product

class ProductModelTest(TestCase):
    
    def test_is_created_product(self):
        
        '''
        Teste reponsavel por verificar a criacao do produto e o uso do metodo da classe
        products, responsavel por setar a categoria do objeto product.
        '''
        
        product_data = {
            'name': 'product_test',
            'price': 10.50,
        }
        
        category_name = 'category_test'
        
        product = Product.objects.create(
            name=product_data['name'],
            price=product_data['price']
        )
        
        product.set_category(category_name)
        
        self.assertEqual(product.category.name, category_name)
        self.assertEqual(product.name, product_data['name'])
