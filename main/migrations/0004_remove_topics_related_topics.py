# Generated by Django 4.2.2 on 2023-09-09 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_topics_attendees_topics_related_topics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topics',
            name='related_topics',
        ),
    ]