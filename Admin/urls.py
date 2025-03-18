from django.urls import path
from Admin import views

app_name = "Admin"

urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),

    path('worker/',views.worker,name="worker"),
    path('deleteworker/<int:id>',views.deleteworker,name="deleteworker"),

    path('admin/',views.admin,name="admin"),
    path('deleteadmin/<int:id>',views.deleteadmin,name="deleteadmin"),
    path('editadmin/<int:id>',views.editadmin,name="editadmin"),

    path('category/',views.category,name="category"),
    path('deletecategory/<int:id>',views.deletecategory,name="deletecategory"),
    path('editcategory/<int:id>',views.editcategory,name="editcategory"),

    path('day/',views.day,name="day"),
    path('deleteday/<int:id>',views.deleteday,name="deleteday"),
    path('editday/<int:id>',views.editday,name="editday"),

    path('ward/',views.ward,name="ward"),
    path('deleteward/<int:id>',views.deleteward,name="deleteward"),
    path('editward/<int:id>',views.editward,name="editward"),

    path("viewcomplaint/",views.viewcomplaint,name="viewcomplaint"),
    path("reply/<int:id>",views.reply,name="reply"),
    path("replyedcomplaint/",views.replyedcomplaint,name="replyedcomplaint"),

    path("viewuser/",views.viewuser,name="viewuser"),
    path("viewfeedback/",views.viewfeedback,name="viewfeedback"),

    path("viewrequest/",views.viewrequest,name="viewrequest"),
    path("acceptrequest/<int:id>",views.acceptrequest,name="acceptrequest"),
    path("collectedwaste/",views.collectedwaste,name="collectedwaste"),

    path("schedule/",views.schedule,name="schedule"),
    path("deleteschedule/<int:id>",views.deleteschedule,name="deleteschedule"),

    path("logout/",views.logout,name="logout"),


]