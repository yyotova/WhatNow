from django.shortcuts import render, get_object_or_404
from users.models import UsersTasks
from users.models import Users
from tasks.models import Tasks


def list(request):
    user = get_object_or_404(Users, user_id=request.session.get('user_id'))
    if request.session.get('user_type') == 3:
        return render(request, 'tasks/list.html', {'tasks': Tasks.objects.filter(status='done').all(), 'user_type': request.session['user_type']}) # noqa
    elif request.session.get('user_type') == 1:
        return render(request, 'tasks/list.html', {'tasks_user': UsersTasks.objects.filter(user_id_id=user).all(), 'user_type': request.session['user_type']}) # noqa
    elif request.session.get('user_type') == 2:
        return render(request, 'tasks/list.html', {'tasks': Tasks.objects.all(), 'user_type': request.session['user_type']}) # noqa
