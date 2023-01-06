from django.contrib import admin
from django.urls import path, include

from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangorest.urls')),
    path('viewset', include(router.urls))
]
