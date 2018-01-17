from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    photo = models.ImageField (null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    com = models.TextField()






    