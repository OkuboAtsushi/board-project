from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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


def good(request, pk):
    post = get_object_or_404(BoardModel, pk=pk)
    post.good += 1
    post.save()
    return redirect('list')


def read(request, pk):
    post = get_object_or_404(BoardModel, pk=pk)
    login_user_id = int(request.user.id)
    read_user_ids = post.read_user_ids.split()
    read_user_ids = [int(id) for id in read_user_ids]
    if login_user_id in read_user_ids:
        return redirect('list')
    post.read += 1
    post.read_user_ids = post.read_user_ids + ' ' + str(login_user_id)
    post.save()
    return redirect('list')


class CreatePost(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ['title', 'author', 'content', 'snsimage']
    success_url = reverse_lazy('list')
