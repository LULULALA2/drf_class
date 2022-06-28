from django.db import models

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    product_name = models.CharField("상품이름", max_length=30)
    thumbnail = models.ImageField("썸네일", blank=True)
    desc = models.TextField("상품설명", max_length=500)
    end_date = models.DateField("종료 일자")
    price = models.IntegerField("가격")
    registration_date = models.DateTimeField("등록시간", auto_now_add=True)
    modified_date = models.DateTimeField("수정시간", auto_now=True)
    is_active = models.BooleanField("활성화 여부", default=True)


class Review(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey(Product, verbose_name="상품", on_delete=models.SET_NULL, null=True)
    desc = models.TextField("내용", max_length=300)
    rating = models.DecimalField("평점", max_digits=2, decimal_places=1)
    created_date = models.DateField("등록날짜", auto_now_add=True)