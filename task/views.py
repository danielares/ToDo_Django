from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, DeleteView
from django.contrib import messages

from .forms import AddTaskForm
from .models import Task

class AddTaskView(CreateView):
    model = Task
    field = '__all__'
    template_name = 'task/add-task.html'
    form_class = AddTaskForm
    success_url = reverse_lazy('add-task')

    
    def post(self, request):
        Task.objects.create(user=request.user,
                            title=request.POST['title'],
                            description=request.POST['description'],
                            due_date=request.POST['due_date'],
                            )
        messages.success(request, 'New Task Created')
        return redirect('index')


class AllMyTasksView(TemplateView):
    template_name = 'task/all-my-tasks.html'
    
    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user = user_id).order_by("due_date")
        return context
    
    
class MyTaskView(TemplateView):
    template_name = 'task/my-task.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_id = context['task_id']
        task = Task.objects.filter(id = task_id)
        task = task[0]
        context['task'] = task
        return context
    
    def post(self, request, task_id):
        task = Task.objects.filter(id = task_id)
        task.update(user=request.user,
                    title=request.POST['title'],
                    description=request.POST['description'],
                    due_date=request.POST['due_date'],)

        messages.success(request, 'Task Updated')
        return redirect('all-my-tasks')
    
    
class DeleteTaskView(TemplateView):
    template_name = 'task/delete-task.html'
    
    def post(self, request, task_id):
        task = Task.objects.filter(id = task_id)
        task.delete()
        messages.success(request, 'Task Deleted')
        return redirect('all-my-tasks')