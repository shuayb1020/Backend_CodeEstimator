from django.urls import path, include
from .models import Project
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'desc', 'file1', 'file2', 'owned_by']
