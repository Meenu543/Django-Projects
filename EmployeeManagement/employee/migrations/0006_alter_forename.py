# Generated by Django 4.1.1 on 2022-09-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_employee_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='forename',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
