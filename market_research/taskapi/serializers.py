from rest_framework import serializers
from .models import Tile, Task

class TileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name="tile-detail")
    # owner = serializers.ReadOnlyField(source='owner.username')
    # or
    # tasks = SimpleTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Tile
        fields = ["id", 'title','status', 'launch_date']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name="task-detail")
    # owner = serializers.ReadOnlyField(source='owner.username')
    # or
    # tasks = SimpleTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ["id", 'title','description', 'order',"type", "tile"
                  ]