from django.contrib import admin
from .models import Post, Category, Image, Comment, Tag, PostTag

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(PostTag)
