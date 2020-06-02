from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


<<<<<<< HEAD
import tasks.views.tasks_view
=======
from tasks.views import tasks, projects, reviews, comments
>>>>>>> 48c809c238835abc03aae81632bf357cdc91a7da
