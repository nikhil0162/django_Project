from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            message = messages.success(request, f'Your account has been cerated {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    form = UserUpdateForm
    return render(request, 'user/profile.html', {'form': form})
