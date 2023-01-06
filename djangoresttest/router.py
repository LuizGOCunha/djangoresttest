from rest_framework import routers

from djangorest.viewset import DummyViewSet

# create router instance
router = routers.DefaultRouter()
# register the router giving it its viewset
# The first argument will be put in the url address, making it possible to register many routes to many models
router.register("dummy", DummyViewSet,)