from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Node, NodeHardware, NodeSoftware


class NodeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'


class NodeHardwareSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = NodeHardware
        fields = '__all__'


class NodeSoftwareSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = NodeSoftware
        fields = '__all__'
