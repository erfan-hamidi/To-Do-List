from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('task/', views.TodoList.as_view(), name= 'todo_list'),
    path('task/<int:pk>', views.TodoDetail.as_view(), name='task'),
    path('task-create/', views.CreateTask.as_view(), name='task-create'),
    path('task-update/<int:pk>',views.UpdateTask.as_view(),name='task-update'),
    path('task-delete/<int:pk>', views.DeleteTask.as_view(), name='task-delete'),
    path('login/', TokenObtainPairView.as_view(),name='login'),
    path('verify/', TokenVerifyView.as_view(), name='verify'),
    path('refresh', TokenRefreshView.as_view(), name='refresh')
]