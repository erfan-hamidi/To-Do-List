from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework import mixins, permissions
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

class CreateTask(generics.CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class UpdateTask(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class DeleteTask(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()