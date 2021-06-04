# Generated by Django 3.1.11 on 2021-05-24 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(editable=False, max_length=255, null=True, unique=True),
        ),
    ]