# Generated by Django 4.2.1 on 2024-01-03 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=30)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
