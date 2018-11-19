from django.db import models
from django.utils import timezone

# Create your models here.

POSITION_CHOICES = (
("0","教授"),
("1","准教授"),
("2","助教授"),
("3","技術職員"),
("4","PD"),
("5","D3"),
("6","D2"),
("7","D1"),
("8","M2"),
("9","M1"),
("10","B4"),
)

list_year = ["01","02","03"]
year = str(timezone.now()).split("-")[0]
month = str(timezone.now()).split("-")[1]

class Member(models.Model):

    def current_year(year,month):
        if month == month in list_year:
            year = str(int(year) - 1)
            return year

    name = models.CharField("氏名",max_length=20)
    publish_name = models.CharField("公開する名前",max_length=20)
    birthplace = models.CharField("出身地",max_length=20,blank=True)
    position = models.CharField("身分",blank=False,max_length=3,choices=POSITION_CHOICES,default="")
    current_year = models.CharField("現在の年度",blank=False,max_length=4,default=year)
    assigned_year = models.CharField("配属された年度",blank=False,max_length=4,default="")
    progress = models.CharField("進路",blank=True,max_length=50,default="宮崎大学工学部→")
    hobby = models.CharField("趣味",blank=True,max_length=100,default="")
    created_at = models.DateTimeField('作成日',default=timezone.now)

    def __str__(self):
        return (self.name)
