# Generated by Django 3.2.9 on 2021-12-13 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=56, null=True, verbose_name='forum_title')),
                ('message', models.TextField(null=True)),
                ('media', models.URLField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Forums',
                'ordering': ['date_created'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.TextField(null=True)),
                ('media', models.URLField(null=True)),
                ('date_replied', models.DateTimeField()),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forum.forum')),
                ('reply_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Replies',
                'ordering': ['date_replied'],
            },
        ),
    ]
