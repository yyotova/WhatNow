from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from users.models import Users


def index(request):
    user = get_object_or_404(User, id=request.session.get('_auth_user_id'))
    request.session['user_id'] = user.id
    user_type = get_object_or_404(Users, user=user)

    request.session['user_type'] = user_type.user_type.id
    return render(request, 'index.html', {'user_type': request.session['user_type']})


from tasks.views import tasks, projects, reviews, comments
