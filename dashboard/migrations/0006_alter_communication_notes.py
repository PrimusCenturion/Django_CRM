# Generated by Django 4.2.7 on 2023-11-29 17:05

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_lead_communications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communication',
            name='notes',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
    ]
