# Generated by Django 3.1.2 on 2020-10-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0009_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('phone', models.CharField(max_length=120, verbose_name='Телефон')),
                ('description', models.TextField(blank=True, max_length=120, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Форма обратной связи',
                'verbose_name_plural': 'Формы обратной связи',
            },
        ),
    ]
