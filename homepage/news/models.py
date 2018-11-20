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
    image = models.ImageField('写真',upload_to='media/',blank=True,default="media/no_image.jpg")
    category = models.ForeignKey(Category,verbose_name='カテゴリ',on_delete=models.PROTECT)
    created_at = models.DateTimeField('作成日',max_length=20,default=timezone.now)

    def __str__(self):
        return self.title


class Blog(models.Model):
    """記事"""
    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')
    category = models.ForeignKey(
        Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    thumnail = models.ImageField(
        'サムネイル', upload_to='post_thumbnail/%Y/%m/%d/', blank=True, null=True)
    is_publick = models.BooleanField('公開可能か?', default=True)
    friend_posts = models.ManyToManyField(
        'self', verbose_name='関連記事', blank=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title

class Image(models.Model):
    """記事に紐づく画像ファイル"""
    title = models.CharField('タイトル', max_length=255, blank=True)
    post = models.ForeignKey(
    Blog, verbose_name='記事', on_delete=models.PROTECT,
    )
    src = models.ImageField('画像', upload_to='images/%Y/%m/%d/', help_text='送信後、一度保存してください。')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return '間接リンク:[filter imgpk]{0}[end] 直接リンク:[filter img]{1}[end]'.format(self.pk, self.src.url)
