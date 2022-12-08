from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
BuyValutAPIView,
WalletViewSet,
SellValutAPIView
)

router = DefaultRouter()
router.register('wallet', WalletViewSet)

urlpatterns = [
    path('buy/', BuyValutAPIView.as_view()),
    path('sell/', SellValutAPIView.as_view()),
    path('', include(router.urls)),
]
