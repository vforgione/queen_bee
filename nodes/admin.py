from django.contrib import admin

from .forms import NodeForm, NodeHardwareForm, NodeSoftwareForm
from .models import Node, NodeHardware, NodeSoftware


class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'state', 'updated_on')
    list_filter = ('tags', 'state', 'created_on', 'updated_on')
    form = NodeForm
    fieldsets = (
        ('General Attributes', {
            'fields': ('id', 'name', 'state', 'description'),
        }),
        ('Location Attributes', {
            'fields': ('longitude', 'latitude', 'address', 'altitude',
                'elevation', 'orientation_x', 'orientation_y', 'orientation_z'),
        }),
        ('Connectivity Attributes', {
            'fields': ('modem_imei', 'sim_iccid', 'ssh_port', 'ssh_key', 'ssl_cert'),
        }),
    )


class NodeHardwareAdmin(admin.ModelAdmin):
    list_display = ('node', 'name', 'expected_state', 'actual_state', 'expected_mode', 'actual_mode', 'updated_on')
    list_filter = ('actual_state', 'actual_mode', 'created_on', 'updated_on')
    form = NodeHardwareForm


class NodeSoftwareAdmin(admin.ModelAdmin):
    list_display = ('node', 'software', 'expected_state', 'actual_state', 'updated_on')
    list_filter = ('actual_state', 'created_on', 'updated_on')
    form = NodeSoftwareForm


admin.site.register(Node, NodeAdmin)
admin.site.register(NodeHardware, NodeHardwareAdmin)
admin.site.register(NodeSoftware, NodeSoftwareAdmin)
