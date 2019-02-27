from django.contrib import admin

from .forms import NodeForm, NodeHardwareForm
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
    list_display = ('name', 'node', 'state', 'mode', 'updated_on')
    list_filter = ('state', 'mode', 'created_on', 'updated_on')
    form = NodeHardwareForm


class NodeSoftwareAdmin(admin.ModelAdmin):
    list_display = ('node', 'software', 'state', 'updated_on')
    lsit_filter = ('state', 'created_on', 'updated_on')


admin.site.register(Node, NodeAdmin)
admin.site.register(NodeHardware, NodeHardwareAdmin)
admin.site.register(NodeSoftware, NodeSoftwareAdmin)
