# Generated by Django 3.1.6 on 2021-02-09 11:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20210209_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=150, null=True, verbose_name='your_comment:'),
        ),
    ]
