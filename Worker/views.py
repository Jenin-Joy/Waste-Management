from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
# Create your views here.

def homepage(request):
    worker = tbl_worker.objects.get(id=request.session["wid"])
    return render(request,"Worker/HomePage.html",{"worker":worker})

def profile(request):
    worker = tbl_worker.objects.get(id=request.session["wid"])
    return render(request,"Worker/MyProfile.html",{"worker":worker})

def editprofile(request):
    worker = tbl_worker.objects.get(id=request.session["wid"])
    if request.method == "POST":
        worker.worker_name = request.POST["txt_name"]
        worker.worker_email = request.POST["txt_email"]
        worker.worker_contact = request.POST["txt_contact"]
        worker.save()
        return render(request,"Worker/MyProfile.html",{"msg":"Profile updated"})
    else:
        return render(request,"Worker/EditProfile.html",{"worker":worker})

def changepassword(request):
    worker = tbl_worker.objects.get(id=request.session["wid"])
    if request.method == "POST":
        old_password = request.POST["txt_old"]
        new_password = request.POST["txt_new"]
        confirm_password = request.POST["txt_con"]
        if worker.worker_password == old_password:
            if new_password == confirm_password:
                worker.worker_password = new_password
                worker.save()
                return render(request,"Worker/MyProfile.html",{"msg":"Password changed"})
            else:
                return render(request,"Worker/ChangePassword.html",{"msg":"Confirm Passwords do not match"})
        else:
            return render(request,"Worker/ChangePassword.html",{"msg":"Old Password is incorrect"})
    else:
        return render(request,"Worker/ChangePassword.html")

def viewrequest(request):
    worker = tbl_worker.objects.get(id=request.session["wid"])
    req = tbl_request.objects.filter(request_status=1,user__ward=worker.ward.id)
    return render(request,"Worker/ViewRequest.html",{"request":req})

def collectrequest(request, id):
    req = tbl_request.objects.get(id=id)
    req.request_status = 2
    req.save()
    return render(request,"Worker/ViewRequest.html",{"msg":"Waste Collected"})

def collectedwaste(request):
    worker = tbl_worker.objects.get(id=request.session["wid"])
    req = tbl_request.objects.filter(request_status=2,user__ward=worker.ward.id)
    return render(request,"Worker/CollectedWaste.html",{"request":req})

def viewschedule(request):
    day = tbl_day.objects.all()
    for i in day:
        i.wards = tbl_schedule.objects.filter(day=i.id)
    return render(request,"Worker/ViewSchedule.html",{"day":day})