# Generated by Django 5.1.5 on 2025-02-09 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_tbl_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_feedback',
            name='user',
        ),
        migrations.DeleteModel(
            name='tbl_complaint',
        ),
        migrations.DeleteModel(
            name='tbl_feedback',
        ),
    ]
