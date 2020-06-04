from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from tasks.models import Tasks, Comments
from users.models import UsersTasks


def list(request):
    return render(request, 'tasks/list.html', {'tasks': Tasks.objects.all()})


def detail(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.session.get('user_type') == 1:
        task.status = 'in progress'
        task.save()
    user_id = request.session.get('user_id')
    comments = Comments.objects.filter(task_id=task_id).all()
    return render(request, 'tasks/detail.html', {'task': task, 'comments': comments, 'user_id': user_id, 'user_type': request.session.get('user_type')}) # noqa


def task_sent_review(request, task_id):
    if request.session.get('user_type') != 1:
        return redirect('/tasks')
    task = get_object_or_404(Tasks, id=task_id)
    task.status = 'review'
    task.save()
    return redirect('/tasks')


def task_close(request, task_id):
    if request.session.get('user_type') != 2:
        return redirect('/tasks')
    task = get_object_or_404(Tasks, id=task_id)
    task.status = 'done'
    task.save()
    return render(request, 'tasks/list.html', {'tasks': Tasks.objects.all()})


class UserForm(forms.ModelForm):
    class Meta:
        model = UsersTasks
        fields = ('user_id',)


def task_asign(request, task_id):
    if request.session.get('user_type') != 2:
        return redirect('/tasks')
    task = get_object_or_404(Tasks, id=task_id)
    task.status = 'pending'
    task.save()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.instance.task_id = task
            form.save()
            return render(request, 'tasks/list.html', {'tasks': Tasks.objects.all()})
    else:
        form = UserForm()
        return render(request, 'tasks/asign.html', {'form': form})


class TaskCreateView(CreateView):
    model = Tasks
    fields = ['title', 'project_id', 'date_start', 'date_end', 'status', 'description']
    template_name = 'tasks/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('tasks:tasks:detail', kwargs={'task_id': self.object.id})
