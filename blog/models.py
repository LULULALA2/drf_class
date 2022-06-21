from django.db import models
import datetime
from datetime import timedelta

# Create your models here.
class Category(models.Model):
    name = models.CharField("이름", max_length=50)
    description = models.TextField("설명")

    def __str__(self):
        return self.name
    

class Article(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    contents = models.TextField("본문")
    startdate =models.DateTimeField("노출 시작", default=datetime.datetime.now())
    enddate = models.DateTimeField("노출 종료", default=(datetime.datetime.now()+timedelta(days=7)))
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} 님이 작성하신 글입니다."


class Comment(models.Model):
    article_id = models.ForeignKey('Article', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    contents = models.TextField("댓글")