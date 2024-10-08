# Generated by Django 4.2.14 on 2024-08-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['pinned', '-created_on']},
        ),
        migrations.AddField(
            model_name='post',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
