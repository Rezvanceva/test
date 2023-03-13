from rest_framework import routers

from shop.views import RetailViewSet

router = routers.SimpleRouter()
router.register('shop', RetailViewSet)

urlpatterns = []
urlpatterns += router.urls
