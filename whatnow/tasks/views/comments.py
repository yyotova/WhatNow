from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from tasks.models import Comments


def list(request):
    return render(request, 'comments/list.html', {'comments': Comments.objects.all()})


def detail(request, comment_id):
    comment = get_object_or_404(Comments, id=comment_id)
    return render(request, 'comments/detail.html', {'comment': comment})


class CommentCreateView(CreateView):
    model = Comments
    fields = ['description', 'date', 'task_id', 'user_id']
    template_name = 'comments/create.html'

    def get_success_url(self, kwargs):
        return reverse_lazy('tasks:comments:detail', kwargs={'comment_id': self.object.id})
