# Generated by Django 3.1.6 on 2021-02-07 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0004_auto_20210207_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
