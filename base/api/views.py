from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes= [
        'GET/api', 
        'GET/api/rooms', 
        'GET/api/rooms/:id', 
    ]
    return Response(routes)

@api_view(['GET'])
def getrooms(request):
    rooms = Room.objects.all()
    Serializer = RoomSerializer(rooms, many=True)
    return Response(Serializer.data)


@api_view(['GET'])
def getroom(request, pk):
    room = Room.objects.get(id=pk)
    Serializer = RoomSerializer(room, many=False)
    return Response(Serializer.data)