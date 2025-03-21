# Generated by Django 5.1.5 on 2025-02-10 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_delete_tbl_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_day')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_ward')),
            ],
        ),
    ]
