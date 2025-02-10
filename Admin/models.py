from django.db import models

# Create your models here.

class tbl_admin(models.Model):
    admin_name = models.CharField(max_length=30)
    admin_email = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=30)

class tbl_category(models.Model):
    category_name = models.CharField(max_length=30)

class tbl_day(models.Model):
    day_name = models.CharField(max_length=30)

class tbl_ward(models.Model):
    ward_name = models.CharField(max_length=30)

class tbl_worker(models.Model):
    worker_name = models.CharField(max_length=30)
    worker_contact = models.CharField(max_length=30)
    worker_email = models.CharField(max_length=30)
    worker_password = models.CharField(max_length=30)
    ward = models.ForeignKey(tbl_ward, on_delete=models.CASCADE)

class tbl_schedule(models.Model):
    ward = models.ForeignKey(tbl_ward, on_delete=models.CASCADE)
    day = models.ForeignKey(tbl_day, on_delete=models.CASCADE)