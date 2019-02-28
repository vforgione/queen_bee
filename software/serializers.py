from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Software


class SoftwareSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'
