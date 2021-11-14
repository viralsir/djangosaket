from django.urls import path
from .views import viewtask,addtask
urlpatterns=[
    path("view/",viewtask,name="view-task"),
    path("new/",addtask,name="add-task")
]