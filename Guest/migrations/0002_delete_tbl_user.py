# Generated by Django 5.1.5 on 2025-02-09 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
        ('User', '0005_remove_tbl_feedback_user_delete_tbl_complaint_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_user',
        ),
    ]
