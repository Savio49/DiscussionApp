# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room

from .serializers import RoomSerializer


@api_view(['GET'])  # list of methods that will be accessible to api users
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    # python dictionaries, lists can be serialized automatically but not objects
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    page = 'rooms'

    rooms = Room.objects.all()
    # many=True allows multiple objects for serialization
    serializer = RoomSerializer(rooms, many=True)

    return Response(serializer.data)
