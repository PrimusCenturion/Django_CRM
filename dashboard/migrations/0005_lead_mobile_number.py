# Generated by Django 4.2.7 on 2023-11-27 15:16

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_lead_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='mobile_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]