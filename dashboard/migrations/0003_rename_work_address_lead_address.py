# Generated by Django 4.2.7 on 2023-11-29 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_lead_work_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='work_address',
            new_name='address',
        ),
    ]
