# Generated by Django 4.2 on 2023-04-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(related_name='post_comments', to='news.comment'),
        ),
    ]
