from django.urls import path
from User import views

app_name = "User"

urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),

    path("profile/",views.profile,name="profile"),
    path("editprofile/",views.editprofile,name="editprofile"),
    path("changepassword/",views.changepassword,name="changepassword"),

    path("complaints/",views.complaints,name="complaints"),
    path("feedback/",views.feedback,name="feedback"),

    path("payment/",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),

    path('sendrequest/',views.sendrequest, name='sendrequest'),
    path('viewschedule/',views.viewschedule, name='viewschedule'),

]