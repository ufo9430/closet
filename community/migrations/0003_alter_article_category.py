# Generated by Django 4.2.2 on 2023-07-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_article_hits_alter_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('notice', '공지사항'), ('talk', '잡담'), ('Q&A', '패션질문')], max_length=50, null=True),
        ),
    ]