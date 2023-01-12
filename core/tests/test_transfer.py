from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import Group
from core.models import Ordinary, CustomUser, Wallet, Shopkeeper
from django.core.management import execute_from_command_line
# Create your tests here.
USERNAME_WITH_PERMISSION = 'Queen'
PASSWORD_WITH_PERMISSION = 'bohemian'
EMAIL_WITH_PERMISSIONS = "queen@gmail.com"
class TransferTestView(TestCase):
    def setUp(self) -> None:
        # Criação dos grupos
        execute_from_command_line(['./manage.py', 'initgroups'])

    def test_send_money_between_profiles(self):
        client = Client()
        CustomUser.objects.create_user(email="wesley@gmail.com", password="123456aa")
        wallet_shopkeeper = Wallet.objects.create(balance=0.0)
        Shopkeeper.objects.create(full_name="maria moura", cpf="12345654556", wallet=wallet_shopkeeper)
        wallet_ordinary = Wallet.objects.create(balance=10.0)
        Ordinary.objects.create(full_name="wesley moura", cpf="12245654556", wallet=wallet_ordinary)
        client.login(email="wesley@gmail.com", password="123456aa")
        data = {
            "value":"10",
            "payer":"12245654556",
            "payee":"12345654556"
        }
        url = reverse("transfer")
        response = client.post(url, data)
        shopkeeper_after = Shopkeeper.objects.get(cpf="12345654556")
        ordinary_after = Ordinary.objects.get(cpf="12245654556")
        self.assertEqual(response.status_code,201)
        self.assertEqual(ordinary_after.wallet.balance, 0)
        self.assertEqual(shopkeeper_after.wallet.balance, 10)




        

