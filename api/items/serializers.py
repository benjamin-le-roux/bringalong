from rest_framework import serializers
from .models import Item, Assignee, Bringing

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class AssigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignee
        fields = '__all__'

class BringingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bringing
        fields = '__all__'