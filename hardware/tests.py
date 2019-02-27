import factory
from django.test import TestCase

from .models import Component, Instance


class ComponentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Component

    name = factory.Faker('name')
    manufacturer = factory.Faker('company')
    version = factory.Faker('pyint')
    is_sensor = False


class InstanceFactory(factory.DjangoModelFactory):
    class Meta:
        model = Instance

    component = factory.SubFactory(ComponentFactory)
    uid = factory.Faker('uuid4')
    calibration = factory.Faker('name')


class InstanceSaveTests(TestCase):
    def test_create(self):
        inst = InstanceFactory()
        self.assertEqual(inst.changesets.count(), 0)

    def test_update(self):
        inst = InstanceFactory()
        original = inst.uid
        inst.uid = 'changed'
        inst.save()

        self.assertEqual(inst.changesets.count(), 1)
        self.assertEqual(inst.changesets.first().changes, {'uid': original})

        original = inst.calibration
        inst.calibration = 'changed'
        inst.save()

        self.assertEqual(inst.changesets.count(), 2)
        self.assertEqual(inst.changesets.first().changes, {'calibration': original})
