from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from audit.mixins import AuditableModel


class SoftwareTypes(DjangoChoices):
    image = ChoiceItem()
    firmware = ChoiceItem()
    driver = ChoiceItem()
    plugin = ChoiceItem()


def software_upload_path(instance: 'Software', filename: str):  # pragma: no cover
    return f'{instance.software.type}/{filename}'


class Software(AuditableModel):
    """Software is any piece of code that runs on the hardware of a node.
    """

    name = models.TextField(null=False)
    version = models.TextField(null=False)
    type = models.TextField(null=False, choices=SoftwareTypes.choices)
    description = models.TextField(null=True, default=None, blank=True)
    source_url = models.TextField(null=True, default=None, blank=True)
    docs_url = models.TextField(null=True, default=None, blank=True)
    source_tarball = models.FileField(null=True, default=None, blank=True, upload_to=software_upload_path)

    # reverse generic relation to changesets
    changesets = GenericRelation('audit.Changeset')

    class Meta:
        # database config
        db_table = 'software'
        unique_together = [('name', 'version')]

        # manager config
        ordering = ('name', '-version')

        # admin config
        verbose_name_plural = 'Software'

    def __str__(self):
        return f'{self.name} {self.version}'
