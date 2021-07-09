import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Task, Tile
from .serializers import TaskSerializer, TileSerializer

client = APIClient()


class TaskTest(APITestCase):
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


class TileTest(APITestCase):
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


class GetAllTilesTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Tile.objects.create(title="Tile A", status=3, launch_date="2026-12-23")
        Tile.objects.create(title="Tile B", status=1, launch_date="2026-11-05")
        Tile.objects.create(title="Tile C", status=2)
        Tile.objects.create(title="Tile D", status=1)

    def test_get_all_tiles(self):
        # use default viewset name
        response = self.client.get(reverse("tile-list"))
        # get data from db
        tiles = Tile.objects.all()
        request = response.wsgi_request

        # context must include request due to HyperlinkedIdentityField
        serializer = TileSerializer(tiles, many=True, context={"request": request})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleTileTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tileA = Tile.objects.create(
            title="Tile A", status=3, launch_date="2026-12-23"
        )
        cls.tileB = Tile.objects.create(
            title="Tile B", status=1, launch_date="2026-11-05"
        )
        cls.tileC = Tile.objects.create(title="Tile C", status=2)
        cls.tileD = Tile.objects.create(title="Tile D", status=2)

    def test_get_valid_single_tile(self):
        response = client.get(reverse("tile-detail", kwargs={"pk": self.tileA.pk}))
        request = response.wsgi_request
        tile = Tile.objects.get(pk=self.tileA.pk)

        # context must include request due to HyperlinkedIdentityField
        serializer = TileSerializer(tile, context={"request": request})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_tile(self):
        response = client.get(reverse("tile-detail", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewTileTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.valid_payload = {
            "title": "Tile A",
            "status": 1,
            "launch_date": "2021-12-23",
        }
        cls.invalid_payload = {
            "title": "",
            "status": 2,
            "launch_date": "2021-12-23",
        }

    def test_create_valid_tile(self):
        self.assertEqual(Tile.objects.count(), 0)
        response = client.post(
            reverse("tile-list"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(Tile.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_tile(self):
        self.assertEqual(Tile.objects.count(), 0)
        response = client.post(
            reverse("tile-list"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(Tile.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleTileTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tileA = Tile.objects.create(title="TileA", status=3)
        cls.tileB = Tile.objects.create(title="TileB", status=2)
        cls.valid_payload = {
            "title": "updated-TileA",
            "status": 2,
            "launch_date": "2025-01-01",
        }
        cls.invalid_payload = {
            "title": "invalid-update",
            "status": 4,
        }

    def test_valid_update_tile(self):
        self.assertEqual(Tile.objects.count(), 2)
        response = client.put(
            reverse("tile-detail", kwargs={"pk": self.tileA.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 204 here?
        self.assertEqual(Tile.objects.count(), 2)

    def test_invalid_update_tile(self):
        self.assertEqual(Tile.objects.count(), 2)
        response = client.put(
            reverse("tile-detail", kwargs={"pk": self.tileB.pk}),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Tile.objects.count(), 2)


class DeleteSingleTileTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tileA = Tile.objects.create(
            title="Tile A", status=3, launch_date="2030-02-14"
        )
        cls.tileB = Tile.objects.create(title="Tile B", status=1)

    def test_valid_delete_tile(self):
        self.assertEqual(Tile.objects.count(), 2)
        response = client.delete(reverse("tile-detail", kwargs={"pk": self.tileB.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tile.objects.count(), 1)

    def test_invalid_delete_tile(self):
        self.assertEqual(Tile.objects.count(), 2)
        response = client.delete(reverse("tile-detail", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Tile.objects.count(), 2)


class GetAllTasksTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_tile = Tile.objects.create(
            title="Tile A", status=3, launch_date="2026-12-23"
        )

        Task.objects.create(
            title="Task A",
            type=3,
            description="description for Task A",
            order=3,
            tile=test_tile,
        )
        Task.objects.create(
            title="Task B",
            type=2,
            description="description for Task B",
            order=4,
            tile=test_tile,
        )
        Task.objects.create(
            title="Task C", type=3, description="description for Task C"
        )
        Task.objects.create(
            title="Task D", type=1, description="description for Task D", tile=test_tile
        )

    def test_get_all_tasks(self):
        response = self.client.get(reverse("task-list"))

        tasks = Task.objects.all()
        request = response.wsgi_request

        # context must include request due to HyperlinkedIdentityField
        serializer = TaskSerializer(tasks, many=True, context={"request": request})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleTaskTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_tile = Tile.objects.create(
            title="Tile A", status=3, launch_date="2026-12-23"
        )

        cls.taskA = Task.objects.create(
            title="Task A",
            type=3,
            description="description for Task A",
            order=3,
            tile=test_tile,
        )
        cls.taskB = Task.objects.create(
            title="Task B",
            type=2,
            description="description for Task B",
            order=4,
            tile=test_tile,
        )
        cls.taskC = Task.objects.create(
            title="Task C", type=3, description="description for Task C"
        )
        cls.taskD = Task.objects.create(
            title="Task D", type=1, description="description for Task D", tile=test_tile
        )

    def test_get_valid_single_task(self):
        response = client.get(reverse("task-detail", kwargs={"pk": self.taskA.pk}))
        request = response.wsgi_request
        task = Task.objects.get(pk=self.taskA.pk)

        # context must include request due to HyperlinkedIdentityField
        serializer = TaskSerializer(task, context={"request": request})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_task(self):
        response = client.get(reverse("task-detail", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewTaskTest(APITestCase):
    @classmethod
    def setUpTestData(cls):

        test_tile = Tile.objects.create(
            title="Tile A", status=3, launch_date="2026-12-23"
        )

        cls.valid_payload = {
            "title": "Task A",
            "description": "new descrition for Task A",
            "order": 2,
            "type": 1,
            "tile": reverse("tile-detail", args=[str(test_tile.id)]),
        }

        cls.invalid_payload = {
            "title": "Task B",
            "description": "",
            "order": 1,
            "type": 1,
            "tile": reverse("tile-detail", args=[str(test_tile.id)]),
        }

    def test_create_valid_task(self):
        self.assertEqual(Task.objects.count(), 0)
        response = client.post(
            reverse("task-list"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_task(self):
        self.assertEqual(Task.objects.count(), 0)
        response = client.post(
            reverse("task-list"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(Task.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleTaskTest(APITestCase):
    @classmethod
    def setUpTestData(cls):

        test_tile = Tile.objects.create(
            title="Tile A", status=3, launch_date="2026-12-23"
        )

        cls.taskC = Task.objects.create(
            title="Task C", type=3, description="description for Task C"
        )
        cls.taskD = Task.objects.create(
            title="Task D", type=1, description="description for Task D", tile=test_tile
        )

        cls.valid_payload = {
            "title": "Task A",
            "description": "new descrition for Task A",
            "order": 1,
            "type": 1,
            "tile": reverse("tile-detail", args=[str(test_tile.id)]),
        }

        cls.invalid_payload = {
            "title": "Task B",
            "description": "invalid payload",
            "order": 1,
            "type": 1,
            "tile": "bad url",
        }

    def test_valid_update_task(self):
        self.assertEqual(Task.objects.count(), 2)
        response = client.put(
            reverse("task-detail", kwargs={"pk": self.taskC.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 204 here?
        self.assertEqual(Task.objects.count(), 2)

    def test_invalid_update_task(self):
        self.assertEqual(Task.objects.count(), 2)
        response = client.put(
            reverse("task-detail", kwargs={"pk": self.taskD.pk}),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 2)


class DeleteSingleTaskTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_tile = Tile.objects.create(
            title="Tile A", status=3, launch_date="2026-12-23"
        )

        cls.taskC = Task.objects.create(
            title="Task C", type=3, description="description for Task C"
        )
        cls.taskD = Task.objects.create(
            title="Task D", type=1, description="description for Task D", tile=test_tile
        )

    def test_valid_delete_task(self):
        self.assertEqual(Task.objects.count(), 2)
        response = client.delete(reverse("task-detail", kwargs={"pk": self.taskC.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)

    def test_invalid_delete_task(self):
        self.assertEqual(Task.objects.count(), 2)
        response = client.delete(reverse("task-detail", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Task.objects.count(), 2)
