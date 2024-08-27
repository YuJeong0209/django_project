from django.contrib import admin
from .models import Post, Comment, Tag
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)