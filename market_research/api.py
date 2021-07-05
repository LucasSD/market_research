from rest_framework import routers
from market_research.taskapi import views as myapp_views

router = routers.DefaultRouter()
router.register('tiles', myapp_views.TileViewset)