from django.db import transaction
from core.models import CustomUser, Ordinary, Shopkeeper
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

    
    def can_create_new_shopkeeper_profiler(self, cpf:str):
        """
            Can create just if dont have a ordinary profile with some cpf
        """
        ordinary_profile_selector = OrdinaryProfileSelector()
        exist = ordinary_profile_selector.check_ordinary_profile_exist_by_cpf(cpf)
        return not(exist)
        