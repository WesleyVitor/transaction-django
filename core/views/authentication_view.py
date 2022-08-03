import json
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.services.authentication_service import AuthenticationService
class LoginApiView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        authentication_service = AuthenticationService()
        try:
            authentication_service.base_authencation(request)
            return Response(data=None, status=status.HTTP_200_OK)
        except Exception:
            return Response(data=None, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        authentication_service = AuthenticationService()
        try:
            authentication_service.logout_user(request)
            return Response(data=None, status=status.HTTP_200_OK)
        except Exception:
            return Response(data=None, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    