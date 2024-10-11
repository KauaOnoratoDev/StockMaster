from django.db import models
import bcrypt


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    '''
    Os metodos dessa classe sao responsaveis por setar uma senha criptografada
    no banco de dados e checar se a senha fornecida pelo usuario é a mesma que
    a senha salva.
    '''
    
    def set_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password = hashed_password.decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __str__(self) -> str:
        return self.username