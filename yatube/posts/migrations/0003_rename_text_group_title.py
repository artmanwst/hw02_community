# Generated by Django 4.1.5 on 2023-01-18 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_group_post_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='text',
            new_name='title',
        ),
    ]
