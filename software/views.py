from rest_framework import viewsets

from .filters import SoftwareFilterset
from .models import Software
from .serializers import SoftwareSerializer


class SoftwareViewset(viewsets.ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    filterset_class = SoftwareFilterset
