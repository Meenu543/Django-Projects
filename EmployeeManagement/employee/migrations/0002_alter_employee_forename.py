# Generated by Django 4.1.1 on 2022-09-23 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='forename',
            field=models.CharField(blank=True, default='', max_length=70),
        ),
    ]
