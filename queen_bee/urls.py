from django.contrib import admin
from django.urls import path, include

from software.routers import router as software_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(software_router.urls)),
]
