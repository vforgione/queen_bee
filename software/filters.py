from django_filters import FilterSet

from .models import Software


_filters = ('exact', 'iexact', 'contains', 'icontains', 'in', 'gt', 'gte', 'lt', 'lte', 'isnull')


class SoftwareFilterset(FilterSet):
    class Meta:
        model = Software
        fields = {
            'name': _filters, 
            'version': _filters, 
            'type': _filters, 
            'created_on': _filters, 
            'updated_on': _filters,
        }
