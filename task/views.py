from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, View, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import AddTaskForm
from .models import Task

@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class AllMyTasksView(TemplateView):
    template_name = 'task/all-my-tasks.html'
    
    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.filter(user = user_id).order_by("due_date")
        for task in tasks:
            if lated_verify(task.due_date):
                task.lated = True
        context['tasks'] = tasks
        
        return context
    

@method_decorator(login_required, name='dispatch')
class UndoneTasksView(TemplateView):
    template_name = 'task/all-my-tasks.html'
    
    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.filter(user = user_id, completed=False).order_by("due_date")
        for task in tasks:
            if lated_verify(task.due_date):
                task.lated = True
        context['tasks'] = tasks
        
        return context
  
    
@method_decorator(login_required, name='dispatch')
class CompleteTasksView(TemplateView):
    template_name = 'task/all-my-tasks.html'
    
    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user = user_id, completed=True).order_by("due_date")
        return context    
    

@method_decorator(login_required, name='dispatch')
class LatedTasksView(TemplateView):
    template_name = 'task/all-my-tasks.html'
    
    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.filter(user = user_id, completed=False).order_by("due_date")
        context_list = []
        for task in tasks:
            if lated_verify(task.due_date):
                task.lated = True
                context_list.append(task)
        context['tasks'] = context_list
        
        return context


@method_decorator(login_required, name='dispatch')    
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


@method_decorator(login_required, name='dispatch') 
class CompleteTaskView(View):
    
    def post(self, request, task_id):
        task = Task.objects.filter(id = task_id)
        if task[0].completed == False:
            task.update(completed=True)
            messages.success(request, 'Task Completed')
        else:
            task.update(completed=False)
            messages.success(request, 'Task Undone')
        return redirect('all-my-tasks')


@method_decorator(login_required, name='dispatch')
class DeleteTaskView(View):
    
    def post(self, request, task_id):
        task = Task.objects.filter(id = task_id)
        task.delete()
        messages.success(request, 'Task Deleted')
        return redirect('all-my-tasks')


def lated_verify(date):
    today = date.today()
    if date < today:
        return True

