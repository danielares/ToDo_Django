from unicodedata import name
from django.urls import path

from .views import AddTaskView, AllMyTasksView, MyTaskView, CompleteTaskView
from .views import DeleteTaskView, UndoneTasksView, CompleteTasksView, LatedTasksView

urlpatterns = [
    path('add-task/', AddTaskView.as_view(), name='add-task'),
    path('all-my-tasks/', AllMyTasksView.as_view(), name='all-my-tasks'),
    path('undone-tasks/', UndoneTasksView.as_view(), name='undone-tasks'),
    path('complete-tasks/', CompleteTasksView.as_view(), name='complete-tasks'),
    path('lated-tasks/', LatedTasksView.as_view(), name='lated-tasks'),
    path('my-task/<int:task_id>', MyTaskView.as_view(), name='my-task'),
    path('complete-task/<int:task_id>', CompleteTaskView.as_view(), name='complete-task'),
    path('delete-task/<int:task_id>', DeleteTaskView.as_view(), name='delete-task'),
]

