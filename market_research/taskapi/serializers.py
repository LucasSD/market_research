from rest_framework import serializers
from .models import Tile

class TileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name="tile-detail")
    # owner = serializers.ReadOnlyField(source='owner.username')
    # or
    # tasks = SimpleTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Tile
        fields = ["id", 'title','status', 'launch_date',
                  ]