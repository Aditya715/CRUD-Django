# Generated by Django 2.2 on 2020-08-09 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0002_auto_20200809_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndianStates',
            fields=[
                ('state', models.CharField(max_length=25, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='requestlist',
            name='request_date',
            field=models.DateField(auto_created=True, default=datetime.date(2020, 8, 9)),
        ),
    ]
