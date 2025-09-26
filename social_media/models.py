from django.db import models

from config import settings


class Post(models.Model):
    text = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="posts/")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
