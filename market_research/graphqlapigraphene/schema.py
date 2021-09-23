import graphene
from graphene_django import DjangoObjectType
from market_research.taskapi.models import Tile, Task


class TileType(DjangoObjectType):
    class Meta:
        model = Tile
        fields = ("title", "status", "launch_date")
        convert_choices_to_enum = False


class TaskType(DjangoObjectType):
    class Meta:
        model = Task

        # type field removed as it causes an error
        fields = ("title", "description", "order", "tile")


class Query(graphene.ObjectType):
    tiles = graphene.List(TileType)
    tasks = graphene.List(TaskType)

    def resolve_tiles(root, info, **kwargs):
        return Tile.objects.all()

    def resolve_tasks(root, info, **kwargs):
        return Task.objects.all()


schema = graphene.Schema(query=Query)
