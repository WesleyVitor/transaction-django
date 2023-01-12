from typing import List
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email', unique=True)
    objects = CustomUserManager()
    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: List[str] = []

    def __str__(self) -> str:
        return self.email
    
class Profile(models.Model):
    full_name = models.CharField('Full Name', max_length=255)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True
    
    def __str__(self) -> str:
        return self.full_name

    def first_name(self):
        first_name = self.full_name.split('')[0]
        return first_name

    def last_name(self):
        last_name = self.full_name.split('')[-1]
        return last_name

class Wallet(models.Model):
    balance = models.DecimalField('Balance', decimal_places=2, max_digits=6)

    
    
    def can_withdraw(self, value):
        if self.balance >= value:
            return True
        
        return False

class Ordinary(Profile):
    wallet = models.OneToOneField(to=Wallet, null=True, on_delete=models.SET_NULL)
    

class Shopkeeper(Profile):
    wallet = models.OneToOneField(to=Wallet, null=True, on_delete=models.SET_NULL)
    

