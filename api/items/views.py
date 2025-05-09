from rest_framework import viewsets
from .models import Item, Assignee, Bringing
from .serializers import ItemSerializer, AssigneeSerializer, BringingSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class AssigneeViewSet(viewsets.ModelViewSet):
    queryset = Assignee.objects.all()
    serializer_class = AssigneeSerializer

class BringingViewSet(viewsets.ModelViewSet):
    queryset = Bringing.objects.all()
    serializer_class = BringingSerializer