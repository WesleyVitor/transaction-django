from django.urls import path
from core.views.ordinary_profile_view import OrdinaryProfileApiView
from core.views.shopkeeper_profile_view import ShopKeeperProfileApiView
from core.views.wallet_transfer_view import WalletTransfer
from core.views.authentication_view import LoginApiView,LogoutApiView
urlpatterns = [
    path('ordinary_profile/', OrdinaryProfileApiView.as_view(), name='index_ordinary_profile'),
    path('shopkeeper_profile/', ShopKeeperProfileApiView.as_view(), name='index_shopkeeper_profile'),
    path('transfer/', WalletTransfer.as_view(), name='transfer'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
]
