# Generated by Django 4.2.7 on 2023-11-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('month', models.CharField(choices=[('1', 'Mr'), ('2', 'Mrs'), ('3', 'Miss'), ('4', 'Ms'), ('5', 'Dr'), ('6', 'Prof')], default='1', max_length=2)),
            ],
        ),
    ]