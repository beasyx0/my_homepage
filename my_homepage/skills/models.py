import uuid
from django.db import models


class SkillsOverview(models.Model):
    '''Skill overview for homepage'''
    overview = models.CharField(max_length=250, help_text='Overview of skills')

    def __str__(self):
        return self.overview[:80]

    class Meta:
        verbose_name_plural = 'Skills Overview'


class Skill(models.Model):
    '''Skill model. Enter skills for viewing on homepage'''
    CATEGORY_CHOICES = (
            ('FRONTEND', 'Frontend'),
            ('BACKEND', 'Backend'),
            ('OTHER', 'Other'),
        )
    category = models.CharField(default='OTHER', max_length=8, choices=CATEGORY_CHOICES, help_text='Category for the skill')
    name = models.CharField(max_length=50, help_text='Name of the skill')
    link = models.URLField(blank=True, help_text='Link to follow for more info on the skill.')
    years_experience = models.IntegerField(blank=True, help_text='Years experience with skill')
    notes = models.CharField(blank=True, default='', max_length=250, help_text='Anything extra worth annotating')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['name', 'category',]
