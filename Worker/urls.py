from django.urls import path
from Worker import views

app_name = "Worker"

urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),

    path("profile/",views.profile,name="profile"),
    path("editprofile/",views.editprofile,name="editprofile"),
    path("changepassword/",views.changepassword,name="changepassword"),

    path("viewrequest/",views.viewrequest,name="viewrequest"),
    path("collectrequest/<int:id>",views.collectrequest,name="collectrequest"),
    path("collectedwaste/",views.collectedwaste,name="collectedwaste"),

    path('viewschedule/',views.viewschedule, name='viewschedule'),
    path('logout/',views.logout, name='logout'),
]