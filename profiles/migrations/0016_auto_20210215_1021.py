# Generated by Django 3.1.6 on 2021-02-15 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_auto_20210215_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
