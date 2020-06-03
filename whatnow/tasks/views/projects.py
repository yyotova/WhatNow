from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from tasks.models import Projects


def list(request):
    if request.session.get('user_type') != 3:
        return redirect('/tasks')
    return render(request, 'projects/list.html', {'projects': Projects.objects.all()})


def detail(request, project_id):
    if request.session.get('user_type') != 3:
        return redirect('/tasks')
    project = get_object_or_404(Projects, id=project_id)
    return render(request, 'projects/detail.html', {'project': project})


class ProjectCreateView(CreateView):
    model = Projects
    fields = ['title', 'date_start', 'date_end', 'description']
    template_name = 'projects/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('tasks:projects:detail', kwargs={'project_id': self.object.id})
