from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ValueListAPIView,
    ValueRetriveAPIView,
    ValueViewSet
)

router = DefaultRouter()
router.register('value', ValueViewSet)



urlpatterns = [
    path('', ValueListAPIView.as_view()),
    path('<int:pk>/', ValueRetriveAPIView.as_view()),
    path('value/', include(router.urls)),

]
