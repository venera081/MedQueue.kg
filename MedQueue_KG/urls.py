from django.contrib import admin
from django.urls import path
from . import drf_yasg

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += drf_yasg.urlpatterns
