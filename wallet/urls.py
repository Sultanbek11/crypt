from django.urls import path, include
from .views import (
Wallet_add,
# BuyAPIView,
)

urlpatterns = [
    path('add/<int:pk>', Wallet_add.as_view()),
    # path('buy/', BuyAPIView.as_view()),
]
