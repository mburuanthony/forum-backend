# Generated by Django 3.2.9 on 2021-12-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='last_edit',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
