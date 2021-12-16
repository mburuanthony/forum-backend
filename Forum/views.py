from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, permissions, filters
from rest_framework.exceptions import NotFound
from .models import Forum, Reply
from .serializers import ForumSerializer, ReplySerializer


class ForumViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

    def get_queryset(self):
        return Forum.objects.all().order_by('-date_created')

    def perform_create(self, serializer):
        forum = serializer.save(created_by=self.request.user)
        return forum

    def destroy(self, request, *args, **kwargs):
        forum = Forum.objects.get(id=self.kwargs['pk'])
        if not forum.created_by == self.request.user:
            raise PermissionDenied('Cannot delete this forum')
        return super().destroy(request, *args, **kwargs)

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'message', 'created_by__username']


class RepliesViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    queryset = Reply.objects.prefetch_related('forum')
    serializer_class = ReplySerializer

    def get_queryset(self):
        forum_pk = self.kwargs.get('forum_pk')
        try:
            Forum.objects.get(pk=forum_pk)
        except Forum.DoesNotExist:
            raise NotFound('reply not found')
        return self.queryset.filter(forum_id=forum_pk).order_by('-date_replied')

    def perform_create(self, serializer):
        forum = Forum.objects.get(pk=self.kwargs['forum_pk'])
        reply = serializer.save(reply_by=self.request.user, forum=forum)
        return reply

    def destroy(self, request, *args, **kwargs):
        reply = Reply.objects.get(pk=self.kwargs['pk'])
        if not reply.reply_by == self.request.user:
            raise PermissionDenied('Cannot delete this reply')
        return super().destroy(request, *args, **kwargs)
