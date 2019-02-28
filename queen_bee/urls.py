from django.contrib import admin
from django.urls import path, include

from software.routers import router as software_router
from hardware.routers import router as hardware_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(software_router.urls)),
    path('api/', include(hardware_router.urls)),
]
