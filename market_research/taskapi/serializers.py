from rest_framework import serializers
from .models import Tile, Task
from rest_framework.validators import UniqueTogetherValidator


class TileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name="tile-detail")

    tasks = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="task-detail"
    )
    # owner = serializers.ReadOnlyField(source='owner.username')
    # or
    # tasks = SimpleTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Tile
        fields = ["id", "title", "status", "launch_date", "tasks"]


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name="task-detail")

    class Meta:
        model = Task
        fields = ["id", "title", "description", "order", "type", "tile"]
        validators = [
            UniqueTogetherValidator(
                queryset=Task.objects.all(), fields=["order", "tile"]
            )
        ]
