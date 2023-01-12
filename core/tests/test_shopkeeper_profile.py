from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import Group
from core.models import Ordinary, CustomUser, Wallet, Shopkeeper
from django.core.management import execute_from_command_line
# Create your tests here.
USERNAME_WITH_PERMISSION = 'Queen'
PASSWORD_WITH_PERMISSION = 'bohemian'
EMAIL_WITH_PERMISSIONS = "queen@gmail.com"
class ShopkeeperProfileTestView(TestCase):
    def setUp(self) -> None:
        # Criação dos grupos
        execute_from_command_line(['./manage.py', 'initgroups'])
    
    def test_list_shopkeeper_created(self):
        client = Client()
        user = CustomUser.objects.create_user(email="wesley@gmail.com", password="123456aa")
        group = Group.objects.get(name="Shopkeeper")
        group.user_set.add(user)
        client.login(email="wesley@gmail.com", password="123456aa")
        response = client.get(reverse("index_ordinary_profile"))
        self.assertEqual(response.status_code, 200)

    def test_should_create_a_shopkeeper_profile(self):
        client = Client()
        shopkeepers_count_before = Shopkeeper.objects.count()
        users_count_before = CustomUser.objects.count()
        wallet_count_before = Wallet.objects.count()
        data = {
            "full_name":"Bernardo",
            "cpf":"19818789098",
            "email":"bernardo@gmail.com",
            "password1":"1234"
        }
        url = reverse("index_shopkeeper_profile")
        response = client.post(url, data)
        self.assertEqual(response.status_code,201)
        self.assertEqual(Shopkeeper.objects.count(), shopkeepers_count_before+1)
        self.assertEqual(CustomUser.objects.count(), users_count_before+1)
        self.assertEqual(Wallet.objects.count(), wallet_count_before+1)




        

