from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Component, Instance


class ComponentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'


class InstanceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Instance
        fields = '__all__'
