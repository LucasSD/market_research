from rest_framework import serializers
from .models import Tile

class TileSerializer(serializers.HyperlinkedModelSerializer):
    
    # owner = serializers.ReadOnlyField(source='owner.username')
    # or
    # tasks = SimpleTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Tile
        fields = ['status', 'launch_date',
                  'title',]