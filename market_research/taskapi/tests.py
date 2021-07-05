from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from .models import Task, Tile
from .serializers import TileSerializer

client = Client()
class TaskTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_tile = Tile.objects.create(title="Some Tile", status=1)
        cls.test_task = Task.objects.create(title="This Task", type=1, tile=test_tile)

        cls.test_task_null_fields = Task.objects.create(title="This Task", type=1)

    def test_title_max_length(self):
        max_length = self.test_task._meta.get_field("title").max_length
        self.assertEqual(max_length, 100)

    def test_description_max_length(self):
        max_length = self.test_task._meta.get_field("description").max_length
        self.assertEqual(max_length, 1000)

    def test_type_choices(self):
        choices = self.test_task._meta.get_field("type").choices
        self.assertEqual(choices, [(1, "Survey"), (2, "Discussion"), (3, "Diary")])

    def test_null_fields(self):
        self.assertEqual(self.test_task_null_fields.tile, None)
        self.assertEqual(self.test_task_null_fields.order, None)

    def test_obj_name(self):  # test __str__
        expected_obj_name = f"{self.test_task.title} -- {self.test_task.type} -- from Tile: {self.test_task.tile.title}"
        self.assertEqual(expected_obj_name, str(self.test_task))


class TileTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_tile = Tile.objects.create(title="Some Tile", status=1)

    def test_status_choices(self):
        choices = self.test_tile._meta.get_field("status").choices
        self.assertEqual(choices, [(1, "Live"), (2, "Pending"), (3, "Archived")])

    def test_title_max_length(self):
        max_length = self.test_tile._meta.get_field("title").max_length
        self.assertEqual(max_length, 100)

    def test_null_fields(self):
        self.assertEqual(self.test_tile.launch_date, None)

    def test_obj_name(self):  # test __str__
        expected_obj_name = f"{self.test_tile.title} -- ID: {self.test_tile.id}"
        self.assertEqual(expected_obj_name, str(self.test_tile))

class GetAllTilesTest(TestCase):
    @classmethod
    def setUpTestDate(cls):
        Tile.objects.create(
        title='Tile A', status=3, launch_date='23/12/2026')
        Tile.objects.create(
        title='Tile B', status=1, launch_date='05/11/2026')
        Tile.objects.create(
        title='Tile C', status=2)
        Tile.objects.create(
        title='Tile D', status=1)

    def test_get_all_tiles(self):
        # get API response
        response = self.client.get(reverse('tiles'))
        # get data from db
        tiles = Tile.objects.all()
        serializer = TileSerializer(tiles, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

