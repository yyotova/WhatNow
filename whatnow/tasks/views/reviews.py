from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

from tasks.models import Tasks
from users.models import Users

from tasks.models import Reviews


def list(request):
    return render(request, 'reviews/list.html', {'reviews': Reviews.objects.all()})


def detail(request, review_id):
    review = get_object_or_404(Reviews, id=review_id)
    return render(request, 'reviews/detail.html', {'review': review})


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('review', 'date',)


def create(request, review_id):
    if request.session.get('user_type') != 2:
        return redirect('/tasks')
    task = get_object_or_404(Tasks, id=review_id)
    user = Users.objects.get(user_id=request.session.get('user_id'))
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.instance.user_id = user
            form.instance.task_id = task
            form.save()
            return redirect('/tasks')
    else:
        form = ReviewForm()
        return render(request, 'reviews/create.html', {'form': form})
