from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from tasks.models import Reviews


def list(request):
    return render(request, 'reviews/list.html', {'reviews': Reviews.objects.all()})


def detail(request, review_id):
    review = get_object_or_404(Reviews, id=review_id)
    return render(request, 'reviews/detail.html', {'review': review})


class ReviewCreateView(CreateView):
    model = Reviews
    fields = ['task_id', 'user_id', 'review', 'date']
    template_name = 'reviews/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('tasks:reviews:detail', kwargs={'review_id': self.object.id})
