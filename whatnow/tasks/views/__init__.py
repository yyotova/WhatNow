
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


from tasks.views import tasks
# , projects, reviews, comments