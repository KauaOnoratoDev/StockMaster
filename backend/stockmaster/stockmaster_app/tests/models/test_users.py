from django.test import TestCase

from ...models import User


class UserModelTestCase(TestCase):
    
    def test__is_created_user(self):
        
        '''
        Este teste é responsavel por testar a criacao de um novo usuario. Verifica
        se os metodos da classe estao funcionando corretamente: (criptografar e checar).
        '''
        
        user_data = {
            'id': 1,
            'username': 'username_test',
            'password': 'password_test',
            'email': 'email_test@test.com',
        }

        user = User.objects.create(
            username=user_data['username'],
            email=user_data['email']
        )
        
        user.set_password(user_data['password'])
        
        self.assertTrue(user.check_password(user_data['password']))
        self.assertFalse(user.check_password('wrong_password'))