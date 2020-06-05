from django.shortcuts import render, get_object_or_404, redirect


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
