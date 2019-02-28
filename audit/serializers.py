from rest_framework.serializers import ModelSerializer

from .models import Changeset


class ChangesetSerializer(ModelSerializer):
    class Meta:
        model = Changeset
        fields = ('changes', 'timestamp')
