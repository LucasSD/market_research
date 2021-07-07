
from django.urls import include, path
from market_research.taskapi import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tiles', views.TileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
