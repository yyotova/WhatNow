from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from tasks.models import Tasks
from tasks.models import Comments


def list(request):
    return render(request, 'tasks/list.html', {'tasks': Tasks.objects.all()})


def detail(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    return render(request, 'tasks/detail.html', {'task': task, 'comments': Comments.objects.filter(task_id=task_id).all()})


class TaskCreateView(CreateView):
    model = Tasks
    fields = ['title', 'project_id', 'date_start', 'date_end', 'status', 'description']
    template_name = 'tasks/create.html'

    def get_success_url(self, kwargs):
        return reverse_lazy('tasks:tasks:detail', kwargs={'task_id': self.object.id})
