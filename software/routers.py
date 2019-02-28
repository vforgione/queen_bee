from rest_framework.routers import DefaultRouter

from .views import SoftwareViewset


router = DefaultRouter(trailing_slash=False)
router.register('software', SoftwareViewset)
