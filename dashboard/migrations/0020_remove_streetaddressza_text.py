# Generated by Django 4.2.7 on 2023-11-29 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_streetaddressza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streetaddressza',
            name='text',
        ),
    ]
