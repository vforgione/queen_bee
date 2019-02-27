from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import JSONField
from django.db import models


class Changeset(models.Model):
    """The Changeset model tracks changes to records in the database.
    If you want to be able to quickly recall changes from a model instance,
    you will need to add a GenericRelation to the model definition:

        from django.contrib.contenttypes.fields import GenericRelation
        from django.db import models

        from autit.mixins import AuditableModel

        class Thing(AuditableModel):
            name = models.TextField()
            changesets = GenericRelation('audit.Changeset')
    """

    # We're going to use a generic relation here so that all
    # the models can dump their changes to a single table, rather
    # than having unique changesets for each model.
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # We store the changed values as a dictionary: if we use
    # django.forms.model_to_dict to serialize each side of the change
    # then we can quickly iterate the new state and check to see if
    # the values are different. If they are then we save the old
    # value in the changes dictionary, and that gets stored here.
    changes = JSONField()

    # ... and timestamp the sucker
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'changesets'
        ordering = ('-timestamp',)
