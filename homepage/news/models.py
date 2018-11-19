from django.db import models
from django.utils import timezone


class Category(models.Model):
    '''カテゴリ'''

    name = models.CharField('カテゴリ名',max_length=255)
    created_at = models.DateTimeField('作成日',default=timezone.now)

    def __str__(self):
        return self.name

class Post(models.Model):
    '''ニュースの記事'''

    title = models.CharField('タイトル',max_length=255)
    text = models.TextField('本文')
    image = models.ImageField('写真',upload_to='media/',blank=True,)
    category = models.ForeignKey(Category,verbose_name='カテゴリ',on_delete=models.PROTECT)
    # date = str(timezone.now()).replace("-",".").split(" ")[0]
    # created_at = models.CharField('作成日',max_length=20,default=date)
    created_at = models.DateTimeField('作成日',max_length=20,default=timezone.now)

    def __str__(self):
        return self.title
