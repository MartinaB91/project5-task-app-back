from django.db import models
from family_member.models import FamilyMember
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    All tasks belongs to a category
    """
    name = models.CharField(max_length=50,  unique=True, blank=False)
    icon = CloudinaryField("category_icon", default="default_image")

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    """
    Family members are allowed to create a task without a end date
    """
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(
            FamilyMember,
            on_delete=models.CASCADE,
            related_name="task_creator",
        )
    category = models.ForeignKey(
            Category,
            on_delete=models.CASCADE,
            related_name="task_category",
            null=False,
            default=None
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    star_points = models.IntegerField(default="0")
    assigned = models.ForeignKey(
            FamilyMember,
            on_delete=models.CASCADE,
            related_name="assigned_family_member",
            null=True,
        )
    
    def __str__(self):
        return f"{self.title}"
