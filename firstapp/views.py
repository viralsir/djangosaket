from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"firstapp/home.html")

def about(request):
    return render(request,"firstapp/aboutus.html")


def greeting(request,name):

    return render(request,"firstapp/greetings.html",{"pathname":name})