from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import AddTaskView, AllMyTasksView, MyTaskView, CompleteTaskView
from .views import DeleteTaskView, UndoneTasksView, CompleteTasksView, LatedTasksView

urlpatterns = [
    path('add-task/', login_required(AddTaskView.as_view()), name='add-task'),
    path('all-my-tasks/', login_required(AllMyTasksView.as_view()), name='all-my-tasks'),
    path('undone-tasks/', login_required(UndoneTasksView.as_view()), name='undone-tasks'),
    path('complete-tasks/', login_required(CompleteTasksView.as_view()), name='complete-tasks'),
    path('lated-tasks/', login_required(LatedTasksView.as_view()), name='lated-tasks'),
    path('my-task/<int:task_id>', login_required(MyTaskView.as_view()), name='my-task'),
    path('complete-task/<int:task_id>', login_required(CompleteTaskView.as_view()), name='complete-task'),
    path('delete-task/<int:task_id>', login_required(DeleteTaskView.as_view()), name='delete-task'),
]

