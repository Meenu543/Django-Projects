# Generated by Django 4.1.1 on 2022-09-24 13:23

from django.db import migrations
from django.core.management import call_command


def populate_area_defaults(apps, schema_editor):
    """Load Data to Add PatientList"""
    call_command("loaddata", "org_data.json", verbosity=2)


class Migration(migrations.Migration):
    dependencies = [
        ('employee', '0003_organization'),
    ]

    operations = [
        migrations.RunPython(populate_area_defaults),
    ]
