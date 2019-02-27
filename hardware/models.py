"""
Hardware is a funny thing in the context of this application. We need to be
able to describe hardware as a somewhat abstract thing, but we also need to
be able to track it as a real thing.

To be able to handle this, we're going to treat hardware as two kinds of records:
`Component` to track the abstract (metadata) and `Instance` to track the real
physical units.
"""

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from audit.mixins import AuditableModel


class Component(AuditableModel):
    """A Component is the abstract information about hardware -- its metadata.
    In this table, we're going to track all the information we need to properly
    describe and qualify a piece of hardware.

    The actual, physical, real world pieces of hardware are `Instance`s.
    """

    # generic metadata
    name = models.TextField(null=False)
    manufacturer = models.TextField(null=False)
    version = models.TextField(null=False)
    part_number = models.TextField(null=True, default=None, blank=True)
    data_sheet = models.URLField(null=True, default=None, blank=True)
    additional_info = models.TextField(null=True, default=None, blank=True)

    # required sensor metadata sentinel
    is_sensor = models.BooleanField(null=False)

    # sensor specific metadata
    parameter = models.TextField(null=True, default=None, blank=True)
    raw_type_summary = models.TextField(null=True, default=None, blank=True)
    raw_data_type = models.TextField(null=True, default=None, blank=True)
    vsr_data_type = models.TextField(null=True, default=None, blank=True)
    vsr_unit = models.TextField(null=True, default=None, blank=True)
    vsr_min_value = models.FloatField(null=True, default=None, blank=True)
    vsr_max_value = models.FloatField(null=True, default=None, blank=True)
    vsr_accuracy = models.FloatField(null=True, default=None, blank=True)
    vsr_context = models.TextField(null=True, default=None, blank=True)

    # reverse generic relation to changesets
    changesets = GenericRelation('audit.Changeset')

    class Meta:
        # database config
        db_table = 'hardware_components'
        unique_together = [('name', 'manufacturer', 'version')]

        # manager config
        ordering = ('name', '-version')

    def __str__(self):
        return f'{self.name} {self.version}'


class Instance(AuditableModel):
    """An Instance is the actual, physical, real world piece of hardware. It
    is unqiuely distinguishable by a given UID.

    For its metadata, see its related `Component`.
    """

    component = models.ForeignKey('hardware.Component', on_delete=models.PROTECT, null=False)
    uid = models.TextField(null=False)
    calibration = models.TextField(null=True, default=None, blank=True)

    # reverse generic relation to changesets
    changesets = GenericRelation('audit.Changeset')

    class Meta:
        # database config
        db_table = 'hardware_instances'
        unique_together = [('component', 'uid')]

        # manager config
        ordering = ('component', 'uid')

    def __str__(self):
        return f'{self.component} :: {self.uid}'
