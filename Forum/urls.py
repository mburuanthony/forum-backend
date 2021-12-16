from django.urls import path
from django.conf.urls import url
from .views import ForumViewset, RepliesViewset

urlpatterns = [
    path('forums/', ForumViewset.as_view({'get': 'list',
         'post': 'create'}), name='list-create-forums'),
    path('forums/<str:pk>/', ForumViewset.as_view(
        {'get': 'retrieve', 'delete': 'destroy'}), name='retrieve-delete-forum'),
    url(r'^forums/(?P<forum_pk>[\w\-]+)/replies/?$', RepliesViewset.as_view(
        {'get': 'list', 'post': 'create'}), name='list-create-forum-replies'),
    url(r'^forums/(?P<forum_pk>[\w\-]+)/replies/(?P<pk>[\w\-]+)?$', RepliesViewset.as_view(
        {'get': 'retrieve', 'delete': 'destroy'}), name='retrieve-delete-reply')
]
