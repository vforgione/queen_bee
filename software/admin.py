from django.contrib import admin

from .forms import SoftwareForm
from .models import Software


class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'type', 'updated_on')
    list_filter = ('type', 'created_on', 'updated_on')
    form = SoftwareForm


admin.site.register(Software, SoftwareAdmin)
