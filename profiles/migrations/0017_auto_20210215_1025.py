# Generated by Django 3.1.6 on 2021-02-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20210215_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
