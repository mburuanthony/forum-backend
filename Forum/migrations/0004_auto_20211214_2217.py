# Generated by Django 3.2.9 on 2021-12-14 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0003_alter_reply_date_replied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='media',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='forum',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='media',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]