# Generated by Django 3.1.2 on 2020-10-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0007_auto_20201012_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='user_avatars/avatar.jpg', null=True, upload_to='user_avatars/', verbose_name='Аватарка'),
        ),
    ]
