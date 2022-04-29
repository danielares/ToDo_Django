from unicodedata import name
from django.urls import path

from .views import AddTaskView, AllMyTasksView, MyTaskView, DeleteTaskView

urlpatterns = [
    path('add-task/', AddTaskView.as_view(), name='add-task'),
    path('all-my-tasks/', AllMyTasksView.as_view(), name='all-my-tasks'),
    path('my-task/<int:task_id>', MyTaskView.as_view(), name='my-task'),
    path('delete-task/<int:task_id>', DeleteTaskView.as_view(), name='delete-task'),
]