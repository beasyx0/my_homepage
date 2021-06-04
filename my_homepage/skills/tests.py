from django.test import TestCase

from my_homepage.skills.models import SkillsOverview, Skill


class TestSkillsOverview(TestCase):
    '''Tests skilloverview model'''

    def test_skillsoverview(self):
        '''Tests the skilloverview model'''

        print('Testing skillsoverview model')

        skillsoverview = SkillsOverview.objects.create(overview='This is an overview')

        self.assertEqual(skillsoverview.__str__(), skillsoverview.overview)
        self.assertEqual(skillsoverview.overview, 'This is an overview')

        print('Finished')

    def test_skill(self):
        '''Tests the skill model'''

        print('Testing skillsoverview model')

        skill = Skill.objects.create(
                    category='FRONTEND',
                    name='Testing',
                    link='https://www.google.com/',
                    years_experience=2,
                    notes='This is a note',
                )

        self.assertEqual(skill.name, skill.__str__())
        self.assertEqual(skill.name, 'Testing')
        self.assertEqual(skill.category, 'FRONTEND')
        self.assertEqual(skill.link, 'https://www.google.com/')
        self.assertEqual(skill.notes, 'This is a note')

        print('Finished')
