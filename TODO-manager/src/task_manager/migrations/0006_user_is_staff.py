# Generated by Django 5.0 on 2024-01-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0005_user_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
