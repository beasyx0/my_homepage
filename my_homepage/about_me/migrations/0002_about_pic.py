# Generated by Django 3.1.11 on 2021-05-24 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='pic',
            field=models.ImageField(default='default-img.jpg', upload_to='pics'),
        ),
    ]
