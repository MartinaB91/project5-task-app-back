from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    """
    All tasks belongs to a category
    """
    name = models.CharField(max_length=50,  unique=True, blank=False)
    icon = CloudinaryField("category_icon", default="default_image")

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"

