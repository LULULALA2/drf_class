# Generated by Django 4.0.5 on 2022-06-27 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30, verbose_name='상품이름')),
                ('thumbnail', models.ImageField(blank=True, upload_to='', verbose_name='썸네일')),
                ('desc', models.TextField(max_length=500, verbose_name='상품설명')),
                ('end_date', models.DateField(verbose_name='종료 일자')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(max_length=300, verbose_name='내용')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='평점')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='등록날짜')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product', verbose_name='상품')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]
