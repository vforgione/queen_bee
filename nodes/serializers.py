from rest_framework import serializers

from .models import Node, NodeHardware, NodeSoftware


class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'


class NodeHardwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NodeHardware
        fields = '__all__'


class NodeSoftwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NodeSoftware
        fields = '__all__'
