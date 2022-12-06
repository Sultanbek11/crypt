from django.urls import path, include
from .views import (
Wallet_add,
# wallet_detail,
)

urlpatterns = [
    path('add/<int:pk>', Wallet_add.as_view()),
    # path('detail/', wallet_detail),
]
