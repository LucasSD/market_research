from django.test import TestCase

from .models import Task

class TaskTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_task = Task()

    def test_title_max_length(self):
        max_length = self.test_task._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_description_max_length(self):
        max_length = self.test_task._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)


