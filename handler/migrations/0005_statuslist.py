# Generated by Django 2.2 on 2020-08-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0004_requestlist_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusList',
            fields=[
                ('status', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]