from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.selectors import ShopKeeperProfileSelector
from core.serializers import OutputShopKeeperProfileSerializer,InputShopkeeperProfileSerializer, InputCustomUserSerializer
from core.services.shopkeeper_profile import ShopkeeperProfileService
class ShopKeeperProfileApiView(APIView):

    def get(self, request):
        shopkeeper_profile_selector =ShopKeeperProfileSelector()
        shopkeepers = shopkeeper_profile_selector.get_all_shopkeeper_profiles()
        if shopkeepers.count == 0:
            return Response(data=None, status=status.HTTP_200_OK)
        shopkeeper_serializers:OutputShopKeeperProfileSerializer = OutputShopKeeperProfileSerializer(shopkeepers, many=True)
        
        return Response(data=shopkeeper_serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        
        shopkeeper_serializer:InputShopkeeperProfileSerializer = InputShopkeeperProfileSerializer(data={
            'full_name':request.data['full_name'],
            'cpf':request.data['cpf']
        })
        user_serializer:InputCustomUserSerializer = InputCustomUserSerializer(data={
            'email':request.data['email'],
            'password1':request.data['password1']
        })
        
        shopkeeper_serializer.is_valid(raise_exception=True)
        user_serializer.is_valid(raise_exception=True)
        shopkeeper_profile_service = ShopkeeperProfileService()
        try:
            shopkeeper_profile_service.create_shopkeeper_profile(shopkeeper_serializer=shopkeeper_serializer,
            user_serializer=user_serializer)
            return Response(status=status.HTTP_201_CREATED)  
        except Exception as e:
            print("msg:",e)
            return Response(data=None, status=status.HTTP_500_INTERNAL_SERVER_ERROR)