# Generated by Django 5.0.2 on 2024-05-09 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_profile_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follows',
        ),
    ]
