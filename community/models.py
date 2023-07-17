from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Article(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    contents = RichTextUploadingField(blank=True, null=True)
    cdate = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    contents = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)