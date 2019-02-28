from rest_framework.routers import DefaultRouter

from .views import ComponentViewset, InstanceViewset


router = DefaultRouter(trailing_slash=False)
router.register('hardware-components', ComponentViewset)
router.register('hardware-instances', InstanceViewset)
