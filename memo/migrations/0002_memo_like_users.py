# Generated by Django 2.2 on 2019-04-24 06:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_memos', to=settings.AUTH_USER_MODEL),
        ),
    ]
