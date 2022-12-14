from django.db import models
from profiles.models import Profile


class FamilyMember(models.Model):
    """
    A family member can have two roles,
    which controlls the priviliges for example a child
    can not create a task. Star points is the total amount
    of scores a family member has been gained by completing tasks.
    """

    ROLE_PRIVILEGE = ((0, "Child"), (1, "Parent"))
    belongs_to_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        default=None,
        null=False,
    )
    name = models.CharField(max_length=255, unique=True, blank=False)
    family_member_img = models.ImageField(
        upload_to="images/",
        default="../rabbit-face-svgrepo-com_frcjxf",
        blank=True,
    )

    role = models.IntegerField(choices=ROLE_PRIVILEGE, default=0)
    star_points = models.IntegerField(default="0")
    ongoing_tasks = models.IntegerField(default="0")
    closed_tasks = models.IntegerField(default="0")

    class Meta:
        verbose_name_plural = "family members"

    def __str__(self):
        return f"{self.name}"
