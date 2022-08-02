from django.urls import path
from core.views import OrdinaryProfileApiView

urlpatterns = [
    path('', OrdinaryProfileApiView.as_view(), name='index'),
]
