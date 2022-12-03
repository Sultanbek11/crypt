from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ValueViewSet,
    Value2ViewSet,
    Value3ViewSet,
    Value4ViewSet,
    Value5ViewSet,
    Value6ViewSet,
    Value7ViewSet,
    Value8ViewSet,
    Value9ViewSet,
    Value10ViewSet,
    Value11ViewSet,
    Value12ViewSet,
)

router = DefaultRouter()
router.register('value', ValueViewSet)
router.register('value2', Value2ViewSet)
router.register('value3', Value3ViewSet)
router.register('value4', Value4ViewSet)
router.register('value5', Value5ViewSet)
router.register('value6', Value6ViewSet)
router.register('value7', Value7ViewSet)
router.register('value8', Value8ViewSet)
router.register('value9', Value9ViewSet)
router.register('value10', Value10ViewSet)
router.register('value11', Value11ViewSet)
router.register('value12', Value12ViewSet)


urlpatterns = [
    path('value/', include(router.urls)),
]
