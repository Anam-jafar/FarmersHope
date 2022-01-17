from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def dashboard(request):
    return render(request, 'Users/dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # to get the data from the form
            messages.success(request, f'Account Created! Now to log in to continue')
            return redirect('login')  # pending should redirect to dashboard of the website

    else:
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'Users/profile.html')
