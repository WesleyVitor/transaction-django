
from core.models import Ordinary


class OrdinaryProfileSelector:

    def get_all_ordinary_profiles(self):
        ordinaries = Ordinary.objects.all()
        return ordinaries