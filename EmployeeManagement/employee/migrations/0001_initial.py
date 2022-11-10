# Generated by Django 4.1.1 on 2022-09-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('forename', models.CharField(blank=True, default='', max_length=60)),
                ('surname', models.CharField(blank=True, default='', max_length=80)),
                ('title', models.CharField(blank=True, default='', max_length=60)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=8)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
