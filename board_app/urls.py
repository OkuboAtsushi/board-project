from django.urls import path

from .views import signup, loginfunc, listfunc, logoutfunc

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
]
