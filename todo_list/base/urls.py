from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.TodoList.as_view(), name= 'todo_list'),
    path('task/<int:pk>', views.TodoDetail.as_view(), name='task'),
    path('task-create/', views.CreateTask.as_view(), name='task-create'),
    path('task-update/<int:pk>',views.UpdateTask.as_view(),name='task-update'),

]