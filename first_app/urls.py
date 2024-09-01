from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
    path('tasks/', TaskListCreateView.as_view(), name='tasks-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-update-delete'),
    path('tasks/statistics/', tasks_statistics, name='tasks-statistics'),
    path('user-tasks/', UserTaskListView.as_view(), name='user-tasks'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-update-delete'),
    path('user-subtasks/', UserSubTaskListView.as_view(), name='user-subtasks'),
]