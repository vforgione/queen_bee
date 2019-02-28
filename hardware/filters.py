from django_filters import FilterSet

from .models import Component, Instance


_filters = ('exact', 'iexact', 'contains', 'icontains', 'in', 'gt', 'gte', 'lt', 'lte', 'isnull')


class ComponentFilterset(FilterSet):
    class Meta:
        model = Component
        fields = {
            'name': _filters,
            'manufacturer': _filters,
            'version': _filters,
            'part_number': _filters,
            'data_sheet': _filters,
            'additional_info': _filters,
            'is_sensor': _filters,
            'parameter': _filters,
            'raw_data_type': _filters,
            'raw_type_summary': _filters,
            'vsr_data_type': _filters,
            'vsr_unit': _filters,
            'vsr_min_value': _filters,
            'vsr_max_value': _filters,
            'vsr_accuracy': _filters,
            'vsr_context': _filters,
        }


class InstanceFilterset(FilterSet):
    class Meta:
        model = Instance
        fields = {
            'uid': _filters,
            'calibration': _filters,
            'component_id': ('exact',)
        }
