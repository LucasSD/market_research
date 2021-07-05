from django.shortcuts import render
from rest_framework import viewsets

from . import models, serializers


class TileViewset(viewsets.ModelViewSet):
    queryset = models.Tile.objects.all()
    serializer_class = serializers.TileSerializer
