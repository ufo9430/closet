# Generated by Django 4.2.2 on 2023-07-13 03:27

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_article_mdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contents',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]