from rest_framework import viewsets

from .filters import ComponentFilterset, InstanceFilterset
from .models import Component, Instance
from .serializers import ComponentSerializer, InstanceSerializer


class ComponentViewset(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    filterset_class = ComponentFilterset


class InstanceViewset(viewsets.ModelViewSet):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
    filterset_class = InstanceFilterset
