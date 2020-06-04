from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from users.models import Users, UsersType


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            dev_type = UsersType.objects.get(pk=1)

            phone = form.cleaned_data.get('phone')

            new_user = Users(user=user, user_type=dev_type, phone=phone)
            new_user.save()

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
