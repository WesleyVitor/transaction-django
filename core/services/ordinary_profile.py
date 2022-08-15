from django.db import transaction
from core.models import CustomUser, Ordinary, Wallet
from core.serializers import InputOrdinaryProfileSerializer, InputCustomUserSerializer
from django.contrib.auth.models import Group
from core.selectors import ShopKeeperProfileSelector

class OrdinaryProfileService:
    @transaction.atomic
    def create_ordinary_profile(self,ordinary_serializer:InputOrdinaryProfileSerializer,user_serializer:InputCustomUserSerializer ):
        if not(self.can_create_new_ordinary_profiler(ordinary_serializer['cpf'].value)):
            raise Exception

        
        user:CustomUser = CustomUser.objects.create_user(email=user_serializer['email'].value, password=user_serializer['password1'].value)
        user.save()
        ordinary:Ordinary = Ordinary.objects.create(full_name=ordinary_serializer['full_name'].value, cpf=ordinary_serializer['cpf'].value, user=user)
        ordinary.save()
        self.ordinary_to_group(user)
        self.create_wallet(ordinary)

    def create_wallet(self, ordinary_profile):
        """ Create a wallet to profile"""
        wallet:Wallet = Wallet.objects.create(balance=0.0)
        wallet.save()
        ordinary_profile.wallet = wallet
        ordinary_profile.save()
    def can_create_new_ordinary_profiler(self, cpf:str):
        """
            Can create just if dont have a shopkeeper profile with some cpf
        """
        shopkeeper_profile_selector = ShopKeeperProfileSelector()
        exist = shopkeeper_profile_selector.check_shopkeeper_profile_exist_by_cpf(cpf)
        return not(exist)

    def ordinary_to_group(self,user):
        ordinary_group_name = "Ordinary"
        group:Group = Group.objects.get(name=ordinary_group_name)
        group.user_set.add(user)
        