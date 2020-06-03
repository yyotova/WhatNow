from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy


from users.models import Users
from users.models import UsersType


def list(request):
    if request.session.get('user_type') != 3:
        return redirect('/')
    else:
        return render(request, 'users/list.html', {'users': Users.objects.all()})


def promote(request, user_id):
    user = get_object_or_404(Users, id=user_id)
    team_leader_type = get_object_or_404(UsersType, id=2)
    user.user_type = team_leader_type
    user.save()
    return render(request, 'users/list.html', {'users': Users.objects.all()})


# class TaskCreateView(CreateView):
#     model = Tasks
#     fields = ['title', 'project_id', 'date_start', 'date_end', 'status', 'description']
#     template_name = 'tasks/create.html'

#     def get_success_url(self, **kwargs):
#         return reverse_lazy('tasks:tasks:detail', kwargs={'task_id': self.object.id})
