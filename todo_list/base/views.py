from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
# Create your views here.
class TodoDetail(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class TodoList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer