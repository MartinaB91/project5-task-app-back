from django.db import models
from cloudinary.models import CloudinaryField


class FamilyMember(models.Model):
    """
    A family member can have two roles, 
    which controlls the priviliges for example a child 
    can not create a task. Star points is the total amount 
    of scores a family member has been gained by completing tasks.
    """
    ROLE_PRIVILEGE = ((0, "Child"), (1, "Parent"))

    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False
        )  
        # TODO: Check if two different profiles can have a family member with the same name (want that to be possible)
    family_member_img = CloudinaryField(
        "family_member_image", 
        default="default_image"
        )
    role = models.IntegerField(choices=ROLE_PRIVILEGE, default=0)
    star_points = models.IntegerField(default="0")
    ongoing_tasks = models.IntegerField(default="0")
    closed_tasks = models.IntegerField(default="0")

    class Meta:
         verbose_name_plural = "family members"

    def __str__(self):
        return f"{self.name}"





