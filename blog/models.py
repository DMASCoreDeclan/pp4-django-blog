from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
APPROVED = ((0, "Not Approved"), (1, "Approved"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_post"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commentor"
        )
    body = models.TextField()
    approved = models.BooleanField(choices=APPROVED, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    
    