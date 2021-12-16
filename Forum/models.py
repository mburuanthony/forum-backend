from django.db import models
import uuid
from django.contrib.auth.models import User


class Forum(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(
        max_length=56, verbose_name='forum_title', null=True)
    message = models.TextField(null=True, blank=True)
    media = models.URLField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    def replies(self):
        return self.reply_set.all()

    class Meta:
        verbose_name_plural = 'Forums'
        ordering = ['date_created']


class Reply(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    reply_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    message = models.TextField(null=True, blank=True)
    media = models.URLField(null=True, blank=True)
    date_replied = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Replies'
        ordering = ['date_replied']
