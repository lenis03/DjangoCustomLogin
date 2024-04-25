from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
        A CustomUser model for manage your website users
    """
    username = None
    phone_number = models.CharField(max_length=11, unique=True)
    otp_code = models.PositiveSmallIntegerField(blank=True, null=True)
    otp_code_created = models.DateTimeField(auto_now_add=True)

    # Other favorite fields...

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = []

    backend = ''
