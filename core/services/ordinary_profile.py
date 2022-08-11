from django.db import transaction
from core.models import CustomUser, Ordinary
from core.serializers import InputOrdinaryProfileSerializer, InputCustomUserSerializer
from django.contrib.auth.models import Group

class OrdinaryProfileService:
    @transaction.atomic
    def create_ordinary_profile(self,ordinary_serializer:InputOrdinaryProfileSerializer,user_serializer:InputCustomUserSerializer ):
        user:CustomUser = CustomUser.objects.create_user(email=user_serializer['email'].value, password=user_serializer['password1'].value)
        user.save()
        ordinary:Ordinary = Ordinary.objects.create(full_name=ordinary_serializer['full_name'].value, cpf=ordinary_serializer['cpf'].value, user=user)
        ordinary.save()
        self.ordinary_to_group(user)

    def ordinary_to_group(self,user):
        ordinary_group_name = "Ordinary"
        group:Group = Group.objects.get(name=ordinary_group_name)
        group.user_set.add(user)
        