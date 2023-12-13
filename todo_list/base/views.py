from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.http import HttpResponse
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer , UserSerializer
from rest_framework import mixins, permissions
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class UserRegistrationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = ()

    def perform_create(self, serializer):
        print("in def/n/n")
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {'refresh': str(refresh), 'access': str(refresh.access_token),}
        return Response(data,status=HTTP_200_OK)

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