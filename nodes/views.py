from .filters import NodeFilterset, NodeHardwareFilterset, NodeSoftwareFilterset
from .models import Node, NodeHardware, NodeSoftware
from .serializers import NodeSerializer, NodeHardwareSerializer, NodeSoftwareSerializer
from audit.mixins import AuditableModelViewSet


class NodeViewset(AuditableModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    filterset_class = NodeFilterset


class NodeHardwareViewset(AuditableModelViewSet):
    queryset = NodeHardware.objects.all()
    serializer_class = NodeHardwareSerializer
    filterset_class = NodeHardwareFilterset


class NodeSoftwareViewset(AuditableModelViewSet):
    queryset = NodeSoftware.objects.all()
    serializer_class = NodeSoftwareSerializer
    filterset_class = NodeSoftwareFilterset
