from django.urls import path
from .views import viewflights,flight_detail
urlpatterns=[
    path("view/",viewflights,name="flight-view"),
    path("detail/<int:id>/",flight_detail,name="flight-detail")
]