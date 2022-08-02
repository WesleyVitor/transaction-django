from django.urls import path
from core.views.ordinary_profile_view import OrdinaryProfileApiView
from core.views.shopkeeper_profile_view import ShopKeeperProfileApiView

urlpatterns = [
    path('ordinary_profile/', OrdinaryProfileApiView.as_view(), name='index_ordinary_profile'),
    path('shopkeeper_profile/', ShopKeeperProfileApiView.as_view(), name='index_shopkeeper_profile'),
]
