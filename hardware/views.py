from .filters import ComponentFilterset, InstanceFilterset
from .models import Component, Instance
from .serializers import ComponentSerializer, InstanceSerializer
from audit.mixins import AuditableModelViewSet


class ComponentViewset(AuditableModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    filterset_class = ComponentFilterset


class InstanceViewset(AuditableModelViewSet):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer
    filterset_class = InstanceFilterset
