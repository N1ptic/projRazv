# models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='articles/')
    content = models.TextField()

    def __str__(self):
        return self.title