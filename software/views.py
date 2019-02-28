from .filters import SoftwareFilterset
from .models import Software
from .serializers import SoftwareSerializer
from audit.mixins import AuditableModelViewSet


class SoftwareViewset(AuditableModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    filterset_class = SoftwareFilterset
