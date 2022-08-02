from rest_framework import serializers

from core.models import Ordinary, Shopkeeper

class InputOrdinaryProfileSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=25)
    cpf =serializers.CharField(max_length=11)
    

class OutputOrdinaryProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordinary
        fields=['id','full_name','cpf']

class InputCustomUserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=200, required=True)
    password1 = serializers.CharField(max_length=200, required=True)

class OutputShopKeeperProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopkeeper
        fields = ('id','full_name', 'cpf')

class InputShopkeeperProfileSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=25)
    cpf =serializers.CharField(max_length=11)