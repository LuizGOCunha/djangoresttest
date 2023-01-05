from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import DummyData
from .serializers import DummySerializer

# Create your views here.

@api_view(['GET',])
def testresponse(request):
    all_objects = DummyData.objects.all()
    serializer = DummySerializer(all_objects, many=True)
    
    return Response(serializer.data)

@api_view(['POST','GET'])
def testresponse_add(request):
    serializer = DummySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)