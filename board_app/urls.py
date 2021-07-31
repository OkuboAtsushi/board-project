from django.urls import path

from .views import signup, loginfunc, listfunc, logoutfunc, detail, good, read

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detail, name='detail'),
    path('good/<int:pk>', good, name='good'),
    path('read/<int:pk>', read, name='read'),
]
