from rest_framework.viewsets import ModelViewSet

from .models import DummyData
from .serializers import DummySerializer

class DummyViewSet(ModelViewSet):
    # Override queryset from modelviewset to show the class all the data it should access
    queryset = DummyData.objects.all()
    # Override serializer_class to show the class which serializer it should use
    serializer_class = DummySerializer
