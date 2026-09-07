from django.contrib import admin
from django.urls import path, include
from . import drf_yasg

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/users/', include('apps.users.urls')),
    # path('api/v1/notifications/', include('apps.notifications.urls')),
    # path('api/v1/clinics', include('apps.clinics.urls')),
    # path('api/v1/appointments', include('apps.appointments.urls'))
]

urlpatterns += drf_yasg.urlpatterns
