from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from audit.mixins import AuditableModel


class Tag(models.Model):
    """A Tag is a tag... we're replacing the old _project_ concept
    and instead using generic tagging to group nodes. It gives us a
    little more cognitive flexibility.
    """

    name = models.TextField(unique=True)

    class Meta:
        db_table = 'tags'


class NodeStates(DjangoChoices):
    build_out = ChoiceItem()
    burn_in = ChoiceItem()
    testing = ChoiceItem()
    storage = ChoiceItem()
    deployed = ChoiceItem()
    decommissioned = ChoiceItem()


class Node(AuditableModel):
    """Nodes are the physical doohickies that tie all the hardware and
    software together into a single, operable unit.
    """

    # general attributes
    id = models.TextField(primary_key=True)
    name = models.TextField(null=True, default=None, blank=True, unique=True)
    state = models.TextField(null=False, choices=NodeStates.choices)
    description = models.TextField(null=True, default=None, blank=True)

    # location attributes
    longitude = models.DecimalField(null=True, default=None, blank=True, decimal_places=10, max_digits=13)
    latitude = models.DecimalField(null=True, default=None, blank=True, decimal_places=10, max_digits=13)
    address = models.TextField(null=True, default=None, blank=True)
    altitude = models.DecimalField(null=True, default=None, blank=True, decimal_places=10, max_digits=13)
    elevation = models.DecimalField(null=True, default=None, blank=True, decimal_places=10, max_digits=13)
    orientation_x = models.DecimalField(null=True, default=None, blank=True, decimal_places=10, max_digits=13)
    orientation_y = models.DecimalField(null=True, default=None, blank=True, decimal_places=10, max_digits=13)
    orientation_z = models.DecimalField(null=True, default=None, blank=True, decimal_places=10, max_digits=13)

    # connectivity attributes
    modem_imei = models.TextField(null=True, default=None, blank=True)
    sim_iccid = models.TextField(null=True, default=None, blank=True)
    ssh_port = models.TextField(null=True, default=None, blank=True)
    ssh_key = models.TextField(null=True, default=None, blank=True)
    ssl_cert = models.TextField(null=True, default=None, blank=True)

    # m2m relationship with tags
    tags = models.ManyToManyField('nodes.Tag')

    # reverse generic relation to changesets
    changesets = GenericRelation('audit.Changeset')

    class Meta:
        # database config
        db_table = 'nodes'

        # manager config
        ordering = ('name',)


class HardwareStates(DjangoChoices):
    on = ChoiceItem()
    off = ChoiceItem()


class HardwareModes(DjangoChoices):
    sd = ChoiceItem()
    emmc = ChoiceItem()


class NodeHardware(AuditableModel):
    """NodeHardware associates hardware instances (the physical device) with
    a node unit.

    The name attribute is there so we can quickly formulate lists of systems
    onboard the nodes: e.g. "node controller" for a C1+, "edge processor" for
    an XU4, "edge processor 2" for an additional XU4.

    The state is a simple on/off toggle for controlling what should be powered
    on at any given time.

    The mode is the boot media mode.
    """

    name = models.TextField(null=False)
    node = models.ForeignKey('nodes.Node', on_delete=models.CASCADE)
    instance = models.OneToOneField('hardware.Instance', on_delete=models.PROTECT)
    state = models.TextField(null=False, choices=HardwareStates.choices)
    mode = models.TextField(null=False, choices=HardwareModes.choices)

    class Meta:
        # database config
        db_table = 'node_hardware'
        unique_together = [('name', 'node', 'instance')]

        # manager config
        ordering = ('node', 'name')

        # admin config
        verbose_name = 'Node Hardware'
        verbose_name_plural = 'Node Hardware'


class SoftwareStates(DjangoChoices):
    running = ChoiceItem()
    stopped = ChoiceItem()


class NodeSoftware(AuditableModel):
    """NodeSoftware tracks the software that is available and on the node.

    The state attribute is an on/off toggle that dictates of the software should
    be actively running on the node.
    """

    node = models.ForeignKey('nodes.Node', on_delete=models.CASCADE)
    software = models.ForeignKey('software.Software', on_delete=models.PROTECT)
    state = models.TextField(null=False, choices=SoftwareStates.choices)

    class Meta:
        # database config
        db_table = 'node_software'
        unique_together = [('node', 'software')]

        # manager config
        ordering = ('node',)

        # admin config
        verbose_name = 'Node Software'
        verbose_name_plural = 'Node Software'
