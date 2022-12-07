from django.urls import path, include
from .views import (
BuyValutAPIView,
# BuyAPIView,
)

urlpatterns = [
    path('buy/', BuyValutAPIView.as_view()),
    # path('buy/', BuyAPIView.as_view()),
]
