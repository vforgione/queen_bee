from django_filters import FilterSet

from .models import Node, NodeHardware, NodeSoftware


_filters = ('exact', 'iexact', 'contains', 'icontains', 'in', 'gt', 'gte', 'lt', 'lte', 'isnull')


class NodeFilterset(FilterSet):
    class Meta:
        model = Node
        fields = {
            'name': _filters,
            'state': _filters,
            'description': _filters,
            'longitude': _filters,
            'latitude': _filters,
            'address': _filters,
            'altitude': _filters,
            'elevation': _filters,
            'orientation_x': _filters,
            'orientation_y': _filters,
            'orientation_z': _filters,
            'modem_imei': _filters,
            'sim_iccid': _filters,
            'ssh_port': _filters,
            'ssh_key': _filters,
            'ssl_cert': _filters,
        }


class NodeHardwareFilterset(FilterSet):
    class Meta:
        model = NodeHardware
        fields = {
            'name': _filters,
            'expected_state': _filters,
            'actual_state': _filters,
            'expected_mode': _filters,
            'actual_mode': _filters,
            'node_id': ('exact',),
            'instance_id': ('exact',),
        }


class NodeSoftwareFilterset(FilterSet):
    class Meta:
        model = NodeSoftware
        fields = {
            'expected_state': _filters,
            'actual_state': _filters,
            'node_id': ('exact',),
            'software_id': ('exact',),
        }
