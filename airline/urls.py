from django.urls import path
from .views import viewflights
urlpatterns=[
    path("view/",viewflights,name="flight-view")
]