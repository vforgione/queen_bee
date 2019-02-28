from rest_framework import serializers

from .models import Software


class SoftwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'
