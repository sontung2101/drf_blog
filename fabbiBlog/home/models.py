from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Create your models here.

class PostModel(models.Model):
    post_title = models.CharField(max_length=100, unique=True)
    content = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True, default=True)
    is_deleted = models.BooleanField(null=True, blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'


class CommentsModel(models.Model):
    content = models.CharField(max_length=255, null=True, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(null=True, blank=True, default=True)
    is_deleted = models.BooleanField(null=True, blank=True, default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comments'
