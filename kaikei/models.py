from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.IntegerField(null=True)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField('名前', max_length=255)
    is_waiting = models.BooleanField('来院中', default=False)

    def __str__(self):
        return 'No.{}: {}'.format(self.customer_id, self.name)    

"""
class WaitingCustomer(models.Model):
   customer = models.ForeignKey(Customer, verbose_name='顧客', blank=False, on_delete=models.PROTECT, limit_choices_to={'is_waiting': True}) 
"""

class Hoken(models.Model):
    name = models.CharField('名前', max_length=255)
    price = models.IntegerField('価格')

    def __str__(self):
        return '{}: {}円'.format(self.name, self.price)

class Jiseki(models.Model):
    name = models.CharField('名前', max_length=255)
    price = models.IntegerField('価格')

    def __str__(self):
        return '{}: {}円'.format(self.name, self.price)

class Buturyou(models.Model):
    name = models.CharField('名前', max_length=255)
    price = models.IntegerField('価格')

    def __str__(self):
        return '{}: {}円'.format(self.name, self.price)

class Shouhin(models.Model):
    name = models.CharField('名前', max_length=255)
    price = models.IntegerField('価格')

    def __str__(self):
        return '{}: {}円'.format(self.name, self.price)

class Product(models.Model):
    hoken = models.ForeignKey(Hoken, verbose_name='保険', blank=False, on_delete=models.PROTECT)
    jiseki = models.ForeignKey(Jiseki, verbose_name='自責', blank=False, on_delete=models.PROTECT)
    buturyou = models.ForeignKey(Buturyou, verbose_name='物療', blank=False, on_delete=models.PROTECT)
    shouhin = models.ForeignKey(Shouhin, verbose_name='商品', blank=False, on_delete=models.PROTECT)

class Payment(models.Model):
    name = models.CharField('支払方法', max_length=255)

    def __str__(self):
        return self.name

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField('名前', max_length=255)

    def __str__(self):
        return 'No.{}: {}'.format(self.staff_id, self.name)

class Choice(models.Model):
    hoken = models.ForeignKey(Hoken, verbose_name='保険', blank=False, on_delete=models.PROTECT)
    hoken_number = models.IntegerField('個数（保険）',default=1, validators=[MinValueValidator(0)])
    hoken_total_score = models.IntegerField('小計（保険）')
    jiseki = models.ForeignKey(Jiseki, verbose_name='自責', blank=False, on_delete=models.PROTECT)
    jiseki_number = models.IntegerField('個数（自責）',default=1, validators=[MinValueValidator(0)])
    jiseki_total_score = models.IntegerField('小計（自責）')
    buturyou = models.ForeignKey(Buturyou, verbose_name='物療', blank=False, on_delete=models.PROTECT)
    buturyou_number = models.IntegerField('個数（物療）',default=1, validators=[MinValueValidator(0)])
    buturyou_total_score = models.IntegerField('小計（物療）')
    shouhin = models.ForeignKey(Shouhin, verbose_name='商品', blank=False, on_delete=models.PROTECT)
    shouhin_number = models.IntegerField('個数（商品）',default=1, validators=[MinValueValidator(0)])
    shouhin_total_score = models.IntegerField('小計（商品）')
    total_score = models.IntegerField('合計')
    customer = models.ForeignKey(Customer, verbose_name='顧客', blank=False, on_delete=models.PROTECT, limit_choices_to={'is_waiting': True})
    created_at = models.DateTimeField('支払日', default=timezone.now)
    payment = models.ForeignKey(Payment, verbose_name='支払方法', blank=False, on_delete=models.PROTECT)
    staff = models.ForeignKey(Staff, verbose_name='担当者', blank=False, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.hoken_total_score = self.hoken.price * self.hoken_number
        self.jiseki_total_score = self.jiseki.price * self.jiseki_number
        self.buturyou_total_score = self.hoken.price * self.buturyou_number
        self.shouhin_total_score = self.hoken.price * self.shouhin_number
        self.total_score = self.hoken_total_score + self.jiseki_total_score + self.buturyou_total_score + self.shouhin_total_score
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}:{}さん({})'.format(self.created_at, self.customer.name, self.id)