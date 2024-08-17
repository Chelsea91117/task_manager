from django.urls import path
from .views import *

urlpatterns = [
    path('greet/<str:name>/', greet, name='greet'),
    path('tasks/', tasks_create_list, name='tasks-create'),
    path('tasks/filter/', tasks_filter_by_status_and_deadline, name='tasks-filter-by-status-and-deadline'),
    path('tasks/statistics/', tasks_statistics, name='tasks-statistics')
]