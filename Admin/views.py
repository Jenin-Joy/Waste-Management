from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Guest.models import *
# Create your views here.

def homepage(request):
    return render(request,"Admin/HomePage.html")

def worker(request):
    worker = tbl_worker.objects.all()
    ward = tbl_ward.objects.all()
    if request.method == 'POST':
        tbl_worker.objects.create(worker_name=request.POST.get('txt_name'),worker_email=request.POST.get('txt_email'),worker_contact=request.POST.get('txt_contact'),worker_password=request.POST.get('txt_password'),ward=tbl_ward.objects.get(id=request.POST.get("sel_ward")))
        return redirect("Admin:worker")
    else:
        return render(request, 'Admin/AddWorker.html', {'worker': worker,"ward":ward})

def deleteworker(request, id):
    tbl_worker.objects.get(id=id).delete()
    return redirect('Admin:worker')

def admin(request):
    admin = tbl_admin.objects.all()
    if request.method == 'POST':
        tbl_admin.objects.create(admin_name=request.POST.get('txt_name'),admin_email=request.POST.get('txt_email'),admin_password=request.POST.get('txt_password'))
        return redirect("Admin:admin")
    else:
        return render(request, 'Admin/AdminReg.html', {'admin': admin})

def deleteadmin(request, id):
    tbl_admin.objects.get(id=id).delete()
    return redirect('Admin:admin')

def editadmin(request, id):
    admin = tbl_admin.objects.get(id=id)
    if request.method == 'POST':
        admin.admin_name = request.POST.get('txt_name')
        admin.admin_email = request.POST.get('txt_email')
        admin.admin_password = request.POST.get('txt_password')
        admin.save()
        return redirect('Admin:admin')
    else:
        return render(request, 'Admin/AdminReg.html', {'editadmin': admin})

def category(request):
    category = tbl_category.objects.all()
    if request.method == 'POST':
        tbl_category.objects.create(category_name=request.POST.get('txt_name'))
        return redirect("Admin:category")
    else:
        return render(request, 'Admin/Category.html', {'category': category})

def deletecategory(request, id):
    tbl_category.objects.get(id=id).delete()
    return redirect('Admin:category')

def editcategory(request, id):
    category = tbl_category.objects.get(id=id)
    if request.method == 'POST':
        category.category_name = request.POST.get('txt_name')
        category.save()
        return redirect('Admin:category')
    else:
        return render(request, 'Admin/Category.html', {'editcategory': category})

def day(request):
    day = tbl_day.objects.all()
    if request.method == 'POST':
        tbl_day.objects.create(day_name=request.POST.get('txt_name'))
        return redirect("Admin:day")
    else:
        return render(request, 'Admin/Day.html', {'day': day})

def deleteday(request, id):
    tbl_day.objects.get(id=id).delete()
    return redirect('Admin:day')

def editday(request, id):
    day = tbl_day.objects.get(id=id)
    if request.method == 'POST':
        day.day_name = request.POST.get('txt_name')
        day.save()
        return redirect('Admin:day')
    else:
        return render(request, 'Admin/Day.html', {'editday': day})

def ward(request):
    ward = tbl_ward.objects.all()
    if request.method == 'POST':
        tbl_ward.objects.create(ward_name=request.POST.get('txt_name'))
        return redirect("Admin:ward")
    else:
        return render(request, 'Admin/Ward.html', {'ward': ward})

def deleteward(request, id):
    tbl_ward.objects.get(id=id).delete()
    return redirect('Admin:ward')

def editward(request, id):
    ward = tbl_ward.objects.get(id=id)
    if request.method == 'POST':
        ward.ward_name = request.POST.get('txt_name')
        ward.save()
        return redirect('Admin:ward')
    else:
        return render(request, 'Admin/Ward.html', {'editward': ward})

def viewcomplaint(request):
    complaint = tbl_complaint.objects.filter(complaint_status=0)
    return render(request,"Admin/ViewComplaint.html",{"complaint":complaint})

def reply(request, id):
    if request.method == "POST":
        complaint = tbl_complaint.objects.get(id=id)
        complaint.complaint_status = 1
        complaint.complaint_reply = request.POST.get("txt_reply")
        complaint.save()
        return render(request,"Admin/Reply.html",{"msg":"Reply Sent"})
    else:
        return render(request,"Admin/Reply.html")

def replyedcomplaint(request):
    complaint = tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/ReplyedComplaint.html",{"complaint":complaint})

def viewuser(request):
    user = tbl_user.objects.all()
    return render(request,"Admin/ViewUser.html",{"user":user})

def viewfeedback(request):
    feedback = tbl_feedback.objects.all()
    return render(request,"Admin/ViewFeedback.html",{"feedback":feedback})

def viewrequest(request):
    req = tbl_request.objects.all()
    return render(request,"Admin/ViewRequest.html",{"request":req})

def acceptrequest(request, id):
    req = tbl_request.objects.get(id=id)
    req.request_status = 1
    req.save()
    return redirect("Admin:viewrequest")

def schedule(request):
    schedule = tbl_schedule.objects.all()
    ward = tbl_ward.objects.all()
    day = tbl_day.objects.all()
    for i in day:
        i.wards = tbl_schedule.objects.filter(day=i.id)
    if request.method == 'POST':
        tbl_schedule.objects.create(day=tbl_day.objects.get(id=request.POST.get('sel_day')),ward=tbl_ward.objects.get(id=request.POST.get('sel_ward')))
        return redirect("Admin:schedule")
    else:
        return render(request,"Admin/Schedule.html",{"schedule":schedule,"ward":ward,"day":day})

def deleteschedule(request, id):
    tbl_schedule.objects.get(id=id).delete()
    return redirect('Admin:schedule')