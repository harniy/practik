# Generated by Django 3.1.2 on 2020-10-10 21:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
                ('url', models.SlugField(max_length=150)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Подкатегория')),
                ('description', models.TextField(default=' ', max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Доп. Категории',
                'verbose_name_plural': 'Доп. Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(max_length=500, verbose_name='Характеристики')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('price', models.SmallIntegerField(default=0, verbose_name='Цена')),
                ('url', models.SlugField(default='', max_length=100)),
                ('poster', models.ImageField(blank=True, upload_to='poster/', verbose_name='Фото')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category', verbose_name='категория')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.subcategory', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Основа',
                'verbose_name_plural': 'Основа',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ManyToManyField(blank=True, to='categories.SubCategory', verbose_name='категория'),
        ),
    ]
