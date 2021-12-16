from rest_framework import serializers
from .models import Forum, Reply
from Auth.serializers import UserSerializer


class ReplySerializer(serializers.ModelSerializer):
    reply_by = UserSerializer(required=False)

    class Meta:
        model = Reply
        fields = ['id', 'reply_by', 'message', 'media', 'date_replied']

        read_only_fields = ['forum']


class ForumSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, required=False)
    created_by = UserSerializer(required=False)

    class Meta:
        model = Forum
        fields = ['id', 'created_by', 'title', 'message',
                  'media', 'date_created', 'last_edit', 'replies']
