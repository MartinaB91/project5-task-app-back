from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    The profile is shared between all family members and each member uses same profile for sign in.

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"
