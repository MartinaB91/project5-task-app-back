from django.db import models
from django.contrib.auth.models import User
from family_member.models import FamilyMember


class Profile(models.Model):
    """
    The profile is shared between all family members and each member uses same profile for sign in. 

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    family_members = models.ForeignKey(
        FamilyMember,
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )


    def __str__(self):
        return f"{self.user}"