from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.users.managers import UserManager
import uuid
from django.conf import settings


class EmailConfirmation(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='email_confirmation'
    )
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'
    

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default='patient')
    phone = models.CharField(max_length=14, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name ='User'
        verbose_name_plural = 'Users'