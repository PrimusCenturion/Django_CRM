# Generated by Django 4.2.7 on 2023-11-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='work_address',
            field=models.ManyToManyField(to='dashboard.zastreetaddress'),
        ),
    ]