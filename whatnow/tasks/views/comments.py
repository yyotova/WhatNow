
from django.urls import reverse_lazy
from tasks.models import Comments, Tasks
from users.models import Users
from django.views.generic import CreateView


class CommentCreate(CreateView):
    model = Comments
    fields = ['description']
    template_name = 'comments/create.html'

    def form_valid(self, form):
        task_id = self.request.get_full_path()[-1::]
        task = Tasks.objects.get(id=task_id)
        user = Users.objects.get(user_id=self.request.session.get('user_id'))
        form.instance.user_id = user
        form.instance.task_id = task
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        task_id = self.request.get_full_path()[-1::]
        return reverse_lazy('tasks:tasks:detail', kwargs={'task_id': task_id})
