from django.db import transaction
from core.models import CustomUser, Ordinary
from core.serializers import InputOrdinaryProfileSerializer, InputCustomUserSerializer


class OrdinaryProfileService:
    @transaction.atomic
    def create_ordinary_profile(self,ordinary_serializer:InputOrdinaryProfileSerializer,user_serializer:InputCustomUserSerializer ):
        user:CustomUser = CustomUser.objects.create_user(email=user_serializer['email'].value, password=user_serializer['password1'].value)
        user.save()
        ordinary:Ordinary = Ordinary.objects.create(full_name=ordinary_serializer['full_name'].value, cpf=ordinary_serializer['cpf'].value, user=user)
        ordinary.save()
        