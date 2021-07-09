from django.urls import include, path
from market_research.taskapi import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"tiles", views.TileViewSet)
router.register(r"tasks", views.TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
