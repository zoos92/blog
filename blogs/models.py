from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """Пост, оставленный пользователем"""
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    date_added =models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """Комментарий к посту"""
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    date_added =models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     verbose_name_plural = 'comments'
    def __str__(self):
        return self.text[:50] + "..."
