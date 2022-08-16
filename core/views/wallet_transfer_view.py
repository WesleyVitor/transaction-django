

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from core.serializers import InputTransfer
from core.services.wallet_transfer_service import WalletTransferService
class WalletTransfer(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        inputTransfer:InputTransfer = InputTransfer(data={
            'value':request.data['value'],
            'payer':request.data['payer'],
            'payee':request.data['payee']
        })

        inputTransfer.is_valid(raise_exception=True)
        walletTransferService = WalletTransferService()
        try:
            walletTransferService.transfer_money(inputTransfer=inputTransfer)
            return Response(status=status.HTTP_201_CREATED)  
        except Exception as e:
            print("EXCEPTION fora:", e)
            return Response(data=None, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        