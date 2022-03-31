from django.contrib import admin

# Register your models here.
from blog.models import Profile, Post, Category, Comment

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
