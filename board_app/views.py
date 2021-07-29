from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from .models import BoardModel


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})


@login_required
def listfunc(request):
    post_list = BoardModel.objects.all()
    return render(request, 'list.html', {'post_list': post_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


@login_required
def detail(request, pk):
    post = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'detail.html', {'post': post})
