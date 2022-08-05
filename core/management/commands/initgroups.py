from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import models as auth_models
class Command(BaseCommand):
    help: str = "Create groups and apply permissions"

    def handle(self, *args, **options):
        
        shopkeeper_group_name = "Shopkeeper"
        ordinary_group_name = "Ordinary"
        shopkeeper_group, created = Group.objects.get_or_create(name=shopkeeper_group_name)
        ordinary_group, created = Group.objects.get_or_create(name=ordinary_group_name)

        can_send_money_name = 'Can Send Money'
        can_receive_money_name = 'Can Receive Money'
        can_send_money_codename = "send_money"
        can_receive_money_codename = "receive_money"
        
        content_type = ContentType.objects.get_for_model(model=auth_models.User)
        
        send_money,created = Permission.objects.get_or_create(name=can_send_money_name, 
        codename=can_send_money_codename,
        content_type=content_type)
        
        receive_money,created = Permission.objects.get_or_create(name=can_receive_money_name,
        codename=can_receive_money_codename,
        content_type=content_type)
        

        shopkeeper_group.permissions.add(receive_money)
        ordinary_group.permissions.add(send_money)
        ordinary_group.permissions.add(receive_money)