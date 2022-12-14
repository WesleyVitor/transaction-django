from django.db import transaction
from django.contrib.auth.models import Group
from core.models import CustomUser, Shopkeeper, Wallet
from core.serializers import InputShopkeeperProfileSerializer, InputCustomUserSerializer
from core.selectors import OrdinaryProfileSelector

class ShopkeeperProfileService:
    @transaction.atomic
    def create_shopkeeper_profile(self,shopkeeper_serializer:InputShopkeeperProfileSerializer,user_serializer:InputCustomUserSerializer ):
        
        if not(self.can_create_new_shopkeeper_profiler(shopkeeper_serializer['cpf'].value)):
            raise Exception

        user:CustomUser = CustomUser.objects.create_user(email=user_serializer['email'].value, 
        password=user_serializer['password1'].value)
        user.save()
        shopkeeper:Shopkeeper = Shopkeeper.objects.create(full_name=shopkeeper_serializer['full_name'].value, 
        cpf=shopkeeper_serializer['cpf'].value, user=user)
        shopkeeper.save()
        self.shopkeeper_to_group(user)
        self.create_wallet(shopkeeper)

    def create_wallet(self, shopkeeper_profile):
        """ Create a wallet to profile"""
        wallet:Wallet = Wallet.objects.create(balance=0.0)
        wallet.save()
        shopkeeper_profile.wallet = wallet
        shopkeeper_profile.save()
    def can_create_new_shopkeeper_profiler(self, cpf:str):
        """
            Can create just if dont have a ordinary profile with some cpf
        """
        ordinary_profile_selector = OrdinaryProfileSelector()
        exist = ordinary_profile_selector.check_ordinary_profile_exist_by_cpf(cpf)
        return not(exist)
    
    def shopkeeper_to_group(self, user):
        shopkeeper_group_name = "Shopkeeper"
        group:Group = Group.objects.get(name=shopkeeper_group_name)
        group.user_set.add(user)
        