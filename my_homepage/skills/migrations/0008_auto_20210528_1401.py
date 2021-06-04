# Generated by Django 3.1.11 on 2021-05-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0007_auto_20210528_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skillsoverview',
            options={'verbose_name_plural': 'Skills Overview'},
        ),
        migrations.RemoveField(
            model_name='skill',
            name='public_id',
        ),
        migrations.AddField(
            model_name='skill',
            name='link',
            field=models.URLField(blank=True, help_text='Link to follow for more info on the skill.'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='years_experience',
            field=models.IntegerField(blank=True, help_text='Years experience with skill'),
        ),
    ]
