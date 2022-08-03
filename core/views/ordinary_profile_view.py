
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


from core.serializers import InputOrdinaryProfileSerializer,OutputOrdinaryProfileSerializer,InputCustomUserSerializer
from core.services.ordinary_profile import OrdinaryProfileService
from core.selectors import OrdinaryProfileSelector
from core.managers import CanCreate
# Create your views here.


class OrdinaryProfileApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated|CanCreate]
    
    def get(self, request):
        ordinary_profile_selector =OrdinaryProfileSelector()
        ordinaries = ordinary_profile_selector.get_all_ordinary_profiles()
        if ordinaries.count == 0:
            return Response(data=None, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        ordinaries_serializer:OutputOrdinaryProfileSerializer = OutputOrdinaryProfileSerializer(ordinaries, many=True)
        
        return Response(data=ordinaries_serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        
        ordinary_serializer:InputOrdinaryProfileSerializer = InputOrdinaryProfileSerializer(data={
            'full_name':request.data['full_name'],
            'cpf':request.data['cpf']
        })
        user_serializer:InputCustomUserSerializer = InputCustomUserSerializer(data={
            'email':request.data['email'],
            'password1':request.data['password1']
        })
        
        ordinary_serializer.is_valid(raise_exception=True)
        user_serializer.is_valid(raise_exception=True)
        ordinary_profile_service = OrdinaryProfileService()
        try:
            ordinary_profile_service.create_ordinary_profile(ordinary_serializer=ordinary_serializer,
            user_serializer=user_serializer)
            return Response(status=status.HTTP_201_CREATED)  
        except Exception as e:
            return Response(data=None, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
       




