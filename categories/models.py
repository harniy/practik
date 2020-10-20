from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class SubCategory(models.Model):
    name = models.CharField('Подкатегория', max_length=100)
    description = models.TextField('Описание', default=' ', max_length=200)

    def get_absolute_url(self):
        return reverse('sub_category', kwargs={'id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доп. Категории'
        verbose_name_plural = 'Доп. Категории'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField('Категория', max_length=100)
    url = models.SlugField(max_length=150)
    parent = models.ManyToManyField(SubCategory, verbose_name='категория', blank=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Main(models.Model):
    name =models.CharField('Имя', max_length=100)
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory,verbose_name='подкатегория', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(default=datetime.now)
    price = models.SmallIntegerField('Цена', default=0)
    url = models.SlugField( default='', max_length=100)
    poster = models.ImageField('Фото', upload_to='poster/', blank=True)


    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug": self.url})

    def get_comment(self):
        return self.comment_set.filter(reply=None).order_by('-id')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Основа'
        verbose_name_plural = 'Основа'

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField('Аватарка', null=True, upload_to='user_avatars/', blank=True, default='user_avatars/avatar.jpg')
    insta = models.CharField('Инстаграм', max_length=200, blank=True)
    facebook = models.CharField('Фейсбук', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Comment(models.Model):
    post = models.ForeignKey(Main, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', null=True, related_name="replies", on_delete=models.CASCADE, blank=True)
    content = models.TextField('Комментарий:', max_length=500)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class FeedBack(models.Model):
    """Форма обратной связи"""
    name = models.CharField('Имя', max_length=120)
    phone = models.CharField('Телефон', max_length=120)
    description = models.TextField('Описание', max_length=120, blank=True, null=True)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'
