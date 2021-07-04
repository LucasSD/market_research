from django.test import TestCase

from .models import Tile, Task


class TaskTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_tile = Tile()
        cls.test_task = Task(title="test_title", type=1, tile=test_tile)

        cls.test_task_no_tile = Task()

    def test_title_max_length(self):
        max_length = self.test_task._meta.get_field("title").max_length
        self.assertEqual(max_length, 100)

    def test_description_max_length(self):
        max_length = self.test_task._meta.get_field("description").max_length
        self.assertEqual(max_length, 1000)

    def test_type_choices(self):
        choices = self.test_task._meta.get_field("type").choices
        self.assertEqual(choices, [(1, "Survey"), (2, "Discussion"), (3, "Diary")])

    def test_tile_null(self):
        self.assertEqual(self.test_task_no_tile.tile, None)

    def test_obj_name(self):  # test __str__
        expected_obj_name = f"{self.test_task.title} {self.test_task.type} {self.test_task.tile}"
        self.assertEqual(expected_obj_name, str(self.test_task))


class TileTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_tile = Tile()

    def test_status_choices(self):
        choices = self.test_tile._meta.get_field("status").choices
        self.assertEqual(choices, [(1, "Live"), (2, "Pending"), (3, "Archived")])
