from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

CATEGORY = (
    ('notice', '공지사항'),
    ('talk', '잡담'),
    ('qna', '패션질문'),
)

class Article(models.Model):
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    contents = RichTextUploadingField(blank=True, null=True)
    cdate = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    contents = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)