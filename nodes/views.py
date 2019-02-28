from rest_framework import viewsets

from .filters import NodeFilterset, NodeHardwareFilterset, NodeSoftwareFilterset
from .models import Node, NodeHardware, NodeSoftware
from .serializers import NodeSerializer, NodeHardwareSerializer, NodeSoftwareSerializer


class NodeViewset(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    filterset_class = NodeFilterset


class NodeHardwareViewset(viewsets.ModelViewSet):
    queryset = NodeHardware.objects.all()
    serializer_class = NodeHardwareSerializer
    filterset_class = NodeHardwareFilterset


class NodeSoftwareViewset(viewsets.ModelViewSet):
    queryset = NodeSoftware.objects.all()
    serializer_class = NodeSoftwareSerializer
    filterset_class = NodeSoftwareFilterset
