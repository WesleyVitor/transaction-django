from django.db import transaction

from core.serializers import InputTransfer
from core.models import Ordinary, Shopkeeper

class WalletTransferService:
    @transaction.atomic
    def transfer_money(self, inputTransfer:InputTransfer):
        value_to_transfer = float(inputTransfer['value'].value)
        ordinary_profile_payer = Ordinary.objects.get(cpf=inputTransfer['payer'].value)
       
        if float(ordinary_profile_payer.wallet.balance) < value_to_transfer:
            raise Exception
        
        try:
            payee = Ordinary.objects.get(cpf=inputTransfer['payee'].value)
        except Exception as e:
            print("Exception dentro:",e)
            payee = Shopkeeper.objects.get(cpf=inputTransfer['payee'].value)


        ordinary_profile_payer.wallet.balance = float(ordinary_profile_payer.wallet.balance) - value_to_transfer
        payee.wallet.balance = float(payee.wallet.balance) + value_to_transfer
        print(ordinary_profile_payer.wallet.balance)
        ordinary_profile_payer.wallet.save()
        payee.wallet.save()