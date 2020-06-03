from django.shortcuts import render, redirect
from users.forms import UserUpdateForm, ProfileUpdateForm
from users.models import Users
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    if request.method == 'POST':
        print(request.user.pk)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            new_phone = u_form.cleaned_data.get('phone')
            p_form.save()
            user = Users.objects.get(user=request.user)
            user.phone = new_phone
            user.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
