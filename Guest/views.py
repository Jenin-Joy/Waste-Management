from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
# Create your views here.

def user(request):
    ward = tbl_ward.objects.all()
    if request.method == 'POST':
        tbl_user.objects.create(user_name=request.POST.get("txt_name"),
                                user_email=request.POST.get("txt_email"),
                                user_password=request.POST.get("txt_password"),
                                user_contact=request.POST.get("txt_contact"),
                                user_address=request.POST.get("txt_address"),
                                user_house_number=request.POST.get("txt_hno"),
                                user_photo=request.FILES.get("txt_photo"),
                                ward=tbl_ward.objects.get(id=request.POST.get("sel_ward")))
        return render(request, 'Guest/UserReg.html',{"msg":"You Registred Sucessfully"})
    else:
        return render(request, 'Guest/UserReg.html',{"ward":ward})

def login(request):
    if request.method == 'POST':
        email = request.POST.get("txt_email")
        password = request.POST.get("txt_password")
        usercount = tbl_user.objects.filter(user_email=email, user_password=password).count()
        admincount = tbl_admin.objects.filter(admin_email=email, admin_password=password).count()
        workercount = tbl_worker.objects.filter(worker_email=email, worker_password=password).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=email, user_password=password)
            request.session["uid"] = user.id
            return redirect("User:homepage")
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=email, admin_password=password)
            request.session["aid"] = admin.id
            return redirect("Admin:homepage")
        elif workercount > 0:
            worker = tbl_worker.objects.get(worker_email=email, worker_password=password)
            request.session["wid"] = worker.id
            return redirect("Worker:homepage")
        else:
            return render(request, 'Guest/Login.html', {"error": "Invalid Email or Password"})
    else:
        return render(request, 'Guest/Login.html')

def index(request):
    return render(request,"Guest/index.html")