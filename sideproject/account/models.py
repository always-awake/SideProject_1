from django.conf import settings
from django.db import models


class Profile(models.Model):
    author = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    phone = models.CharField(max_length=11, blank=True)
    birth = models.DateField(null=True)
    