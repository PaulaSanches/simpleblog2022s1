from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    website_url=models.CharField(max_length=200, null=True, blank=True)
    github_url = models.CharField(max_length=200, null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    title_tag = models.CharField(max_length=50, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="postauthor")
    body = models.TextField()
    post_created_date = models.DateTimeField(auto_now_add=True)
    post_updated_date = models.DateTimeField(auto_now=True)
    snippet = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="postcategory")
    likes = models.ManyToManyField(User, related_name="postlikes")

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commentpost")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentuser")
    body = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)



