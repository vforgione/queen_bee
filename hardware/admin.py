from django.contrib import admin

from .forms import ComponentForm, InstanceForm
from .models import Component, Instance


class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'manufacturer', 'is_sensor', 'updated_on')
    list_filter = ('is_sensor', 'created_on', 'updated_on')
    form = ComponentForm
    fieldsets = (
        ('General Information', {
            'fields': ('name', 'manufacturer', 'version', 'part_number', 
                'data_sheet', 'additional_info'),
        }),
        ('Is this component a sensor?', {
            'fields': ('is_sensor',),
        }),
        ('Sensor Metadata', {
            'fields': ('parameter', 'raw_type_summary', 'raw_data_type',
                'vsr_data_type', 'vsr_unit', 'vsr_min_value', 'vsr_max_value',
                'vsr_accuracy', 'vsr_context'),
        }),
    )


class InstanceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'calibration', 'updated_on')
    list_filter = ('created_on', 'updated_on')
    form = InstanceForm


admin.site.register(Component, ComponentAdmin)
admin.site.register(Instance, InstanceAdmin)
