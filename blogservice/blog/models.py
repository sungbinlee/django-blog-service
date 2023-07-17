from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    is_email_verified = models.BooleanField(default=False)
    social_provider = models.CharField(max_length=255, blank=True)
    social_id = models.CharField(max_length=255, blank=True)
    profile_picture = models.CharField(max_length=255, blank=True)
    introduction = models.CharField(max_length=255, blank=True)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class CommentLike(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
