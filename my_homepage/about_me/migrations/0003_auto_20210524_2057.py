# Generated by Django 3.1.11 on 2021-05-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0002_about_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='about',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]