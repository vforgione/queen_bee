from rest_framework.routers import DefaultRouter

from .views import NodeViewset, NodeHardwareViewset, NodeSoftwareViewset


router = DefaultRouter(trailing_slash=False)
router.register('nodes', NodeViewset)
router.register('node-hardware', NodeHardwareViewset)
router.register('node-software', NodeSoftwareViewset)
