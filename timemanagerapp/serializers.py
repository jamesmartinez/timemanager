from rest_framework import serializers

from timemanagerapp.models import Entry
from timemanagerapp.models import Task


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task

