# Generated by Django 4.2.7 on 2023-11-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_socialmedialink'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='social_media_links',
            field=models.ManyToManyField(to='dashboard.socialmedialink'),
        ),
    ]
