from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.TodoList.as_view(),name= 'todo_list')
]