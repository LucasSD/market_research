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
    tile = graphene.Field(TileType, title=graphene.String())

    tasks = graphene.List(TaskType)
    task = graphene.List(TaskType, title=graphene.String())

    def resolve_tiles(root, info, **kwargs):
        return Tile.objects.all()

    def resolve_tile(self, info, title):
        return Tile.objects.get(title=title)

    def resolve_tasks(root, info, **kwargs):
        return Task.objects.all()

    def resolve_task(self, info, title):
        return Task.objects.filter(title=title)


schema = graphene.Schema(query=Query)
