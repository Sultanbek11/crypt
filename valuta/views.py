from rest_framework import viewsets, generics
from .models import Value
from .serializers import ValueSerializer


class ValueViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()[:100]
    serializer_class = ValueSerializer


class Value2ViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()[100:201]
    serializer_class = ValueSerializer


class Value3ViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()[200:301]
    serializer_class = ValueSerializer


class Value4ViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()[300:401]
    serializer_class = ValueSerializer


class Value5ViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()[400:501]
    serializer_class = ValueSerializer


class Value6ViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()[500:601]
    serializer_class = ValueSerializer


class Value7ViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()[600:701]
    serializer_class = ValueSerializer


class Value8ViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()[700:801]
    serializer_class = ValueSerializer


class Value9ViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()[800:901]
    serializer_class = ValueSerializer


class Value10ViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()[900:1001]
    serializer_class = ValueSerializer


class Value11ViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()[1000:1101]
    serializer_class = ValueSerializer


class Value12ViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()[1100:]
    serializer_class = ValueSerializer
