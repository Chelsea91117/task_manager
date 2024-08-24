from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='tasks-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-update-delete'),
    path('tasks/statistics/', tasks_statistics, name='tasks-statistics'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-update-delete'),
]