from django.contrib import admin
from apps.users.models import CustomUser, EmailConfirmation

admin.site.register(CustomUser)
admin.site.register(EmailConfirmation)
