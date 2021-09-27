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
        fields = ("title", "description", "order", "kind", "tile",)
        convert_choices_to_enum = False


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


class TileInput(graphene.InputObjectType):
    title = graphene.String()
    status = graphene.Int()
    launchDate = graphene.Date()


class CreateTile(graphene.Mutation):
    class Arguments:
        input = TileInput(required=True)

    tile = graphene.Field(TileType)

    @classmethod
    def mutate(cls, root, info, input):
        tile = Tile()
        tile.title = input.title
        tile.status = input.status
        tile.launchDate = graphene.Date(input.launchDate)

        tile.save()
        return CreateTile(tile=tile)


class TaskInput(graphene.InputObjectType):
    title = graphene.String()
    description = graphene.String()
    order = graphene.Int()
    kind = graphene.Int()


class CreateTask(graphene.Mutation):
    class Arguments:
        input = TaskInput(required=True)

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, input):
        task = Task()
        task.title = input.title
        task.description = input.description
        task.order = input.order
        task.kind = input.kind

        task.save()
        return CreateTask(task=task)


class Mutation(graphene.ObjectType):
    create_tile = CreateTile.Field()
    create_task = CreateTask.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
