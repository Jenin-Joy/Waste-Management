from django.db import models
from Guest.models import *
# Create your models here.

class tbl_complaint(models.Model):
    complaint_title = models.CharField(max_length=30)
    complaint_content = models.CharField(max_length=200)
    complaint_reply = models.CharField(max_length=200)
    complaint_status = models.IntegerField(default=0)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_content = models.CharField(max_length=30)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_payment(models.Model):
    payment_amount = models.FloatField(default=100)
    payment_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_request(models.Model):
    request_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    category = models.ForeignKey(tbl_category, on_delete=models.CASCADE)
    request_content = models.CharField(max_length=100)
    request_status = models.IntegerField(default=0)