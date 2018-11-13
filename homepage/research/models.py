from django.db import models

# Create your models here.

class Research(models.Model):
    title = models.CharField("タイトル",max_length=30)
    text = models.TextField("内容")

    def __str__(self):
        return self.title
