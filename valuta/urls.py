from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ValutaListAPIView


router = DefaultRouter

urlpatterns = [
    path('', ValutaListAPIView.as_view()),
]
