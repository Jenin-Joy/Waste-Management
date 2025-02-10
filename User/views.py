from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from User.models import *
from datetime import date
# Create your views here.

def homepage(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/HomePage.html",{"user":user})

def profile(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{"user":user})

def editprofile(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    if request.method == "POST":
        user.user_name = request.POST["txt_name"]
        user.user_email = request.POST["txt_email"]
        user.user_contact = request.POST["txt_contact"]
        user.user_address = request.POST["txt_address"]
        user.save()
        return render(request,"User/MyProfile.html",{"msg":"Profile updated"})
    else:
        return render(request,"User/EditProfile.html",{"user":user})

def changepassword(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    if request.method == "POST":
        old_password = request.POST["txt_old"]
        new_password = request.POST["txt_new"]
        confirm_password = request.POST["txt_con"]
        if user.user_password == old_password:
            if new_password == confirm_password:
                user.user_password = new_password
                user.save()
                return render(request,"User/MyProfile.html",{"msg":"Password changed"})
            else:
                return render(request,"User/ChangePassword.html",{"msg":"Confirm Passwords do not match"})
        else:
            return render(request,"User/ChangePassword.html",{"msg":"Old Password is incorrect"})
    else:
        return render(request,"User/ChangePassword.html")

def complaints(request):
    complaint = tbl_complaint.objects.filter(user=request.session["uid"])
    if request.method == "POST":
        tbl_complaint.objects.create(complaint_title=request.POST.get("txt_title"),complaint_content=request.POST.get("txt_content"),user=tbl_user.objects.get(id=request.session["uid"]))
        return render(request,"User/Complaint.html",{"msg":"Complaint Send Sucessfully.."})
    else:
        return render(request,"User/Complaint.html",{"complaint":complaint})

def feedback(request):
    if request.method == "POST":
        tbl_feedback.objects.create(feedback_content=request.POST.get("txt_content"),user=tbl_user.objects.get(id=request.session["uid"]))
        return render(request,"User/Feedback.html",{"msg":"Feedback Send Sucessfully.."})
    else:
        return render(request,"User/Feedback.html")

def payment(request):
    if request.method == "POST":
        count = tbl_payment.objects.filter(user=request.session["uid"],payment_date__month=date.today().month).count()
        if count > 0:
            return render(request,"User/Payment.html",{"msg":"Payment Already Done.."})
        else:
            tbl_payment.objects.create(user=tbl_user.objects.get(id=request.session["uid"]))
            return redirect("User:loader")
    else:
        return render(request,"User/Payment.html")

def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Paymentsuc.html")

def sendrequest(request):
    category = tbl_category.objects.all()
    userrequest  = tbl_request.objects.filter(user=request.session["uid"])
    if request.method == "POST":
        tbl_request.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),category=tbl_category.objects.get(id=request.POST.get("sel_category")),request_content=request.POST.get("txt_content"))
        return render(request,"User/SendRequest.html",{"msg":"Request sent successfully"})
    else:
        return render(request,"User/SendRequest.html",{"category":category,"request":userrequest})

def viewschedule(request):
    day = tbl_day.objects.all()
    for i in day:
        i.wards = tbl_schedule.objects.filter(day=i.id)
    return render(request,"User/ViewSchedule.html",{"day":day})