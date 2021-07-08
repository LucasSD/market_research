from django.shortcuts import render
from rest_framework import viewsets

from . import models, serializers


class TileViewSet(viewsets.ModelViewSet):
    queryset = models.Tile.objects.all()
    serializer_class = serializers.TileSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
