from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)
