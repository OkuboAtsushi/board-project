from django.urls import path

from .views import signup, listfunc

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('list/', listfunc, name='list'),
]
