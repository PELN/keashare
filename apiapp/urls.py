from rest_framework.routers import SimpleRouter
from .views import GroupViewSet

router = SimpleRouter()
router.register('groupslist', GroupViewSet, base_name='groupslist') # register endpoint and viewset

urlpatterns = router.urls