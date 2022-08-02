
from core.models import Ordinary, Shopkeeper


class OrdinaryProfileSelector:

    def get_all_ordinary_profiles(self):
        ordinaries = Ordinary.objects.all()
        return ordinaries
    
    def check_ordinary_profile_exist_by_cpf(self, cpf:str):
        return Ordinary.objects.filter(cpf=cpf).exists()
class ShopKeeperProfileSelector:

    def get_all_shopkeeper_profiles(self):
        shopkeepers = Shopkeeper.objects.all()
        return shopkeepers