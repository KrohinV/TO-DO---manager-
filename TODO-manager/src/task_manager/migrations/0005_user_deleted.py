# Generated by Django 5.0 on 2024-01-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0004_alter_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
