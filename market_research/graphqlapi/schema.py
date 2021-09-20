import typing
import strawberry

@strawberry.type
class Tile:
    title: str

    status: int

    launch_date: str

@strawberry.type
class Task:
    title: str

    description: str

    order: int

    type: int

    tile: