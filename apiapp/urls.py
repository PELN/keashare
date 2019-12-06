# from rest_framework import routers
from rest_framework.routers import SimpleRouter
from .views import GroupViewSet

# app_name = 'apiapp'

router = SimpleRouter()
router.register('groupslist', GroupViewSet, base_name='groupslist')

urlpatterns = router.urls

