from django.db import models, transaction
from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import ChangesetSerializer


class AuditableModel(models.Model):
    """AuditableModel is an abstract mixin model that 
    automatically stores changes to records in the changeset table.
    """

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # First things first, and this is really something that irks me
        # to no end with django, we want to clean the instance to ensure
        # that its fields only have correct, casted values and it's been
        # fully validated. Why the ORM doesn't do this automatically and
        # leaves this as a "you can call it yourself if you want to" kind
        # of thing is just infuriating.
        self.full_clean()

        # Check to see if this is a create or update... again, a modern,
        # sane ORM would separate these functions.
        if not self.pk:
            super().save(*args, **kwargs)
        else:
            # We need to get the stored record from the database
            from_db = self.__class__.objects.get(pk=self.pk)

            # And then cast the values into dictionaries so we can compare
            # them more easily. This is now a safe comparison since we called
            # full clean -- for example, if for some reason we had and integer
            # field saved as `5` and the instance version were `"5"` the
            # diff would say that the field was changed, even though the database
            # would have cast the string to an int, and nothing would have
            # been changed.
            db_dict = model_to_dict(from_db)
            instance_dict = model_to_dict(self)

            # Iterate over the instance dictionary and compare the values.
            # If the db dictionary's value is different from the instance
            # value, we need to store the db value in the changes dict.
            changes = {}
            for key, instance_value in instance_dict.items():
                db_value = db_dict[key]
                if db_value != instance_value:
                    changes[key] = {'from': db_value, 'to': instance_value}

            # Now we are free to save the instance, but we also want to
            # save the changes in a single transaction.
            from .models import Changeset

            with transaction.atomic():
                super().save(*args, **kwargs)
                Changeset.objects.create(content_object=self, changes=changes)


class AuditableModelViewSet(ModelViewSet):

    @action(detail=True, methods=['get'])
    def changesets(self, request, pk):
        obj = self.get_object()
        serialized = [ChangesetSerializer(instance=c).data for c in obj.changesets.all()]
        return Response({'results': serialized})
