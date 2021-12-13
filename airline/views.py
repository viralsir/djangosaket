from django.shortcuts import render
from .models import flight
from django.http import JsonResponse
# Create your views here.

#airline/page/1
def viewflights(request,page):
    flightlist=flight.objects.all()[page-1*10:page*10]
    #return JsonResponse({"data":flightlist})
    return render(request,"airline/flightlist.html",{
        "flightlist":flightlist
    })

# flight/detail/<id>
def flight_detail(request,id):
    flightinfo=flight.objects.get(pk=id)
    # #flightinfo.values();
    # a={"data":flightinfo.value()}
    # return JsonResponse(a)
    return render(request,"airline/flight_detail.html",{
        "flightinfo":flightinfo
    })

