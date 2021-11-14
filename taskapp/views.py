from django.shortcuts import render,redirect

tasks=["check balance","recharge phone","book movie ticket"]


# Create your views here.
def viewtask(request):
    return  render(request,"taskapp/viewtask.html",{
        "tasks":tasks
    })

def addtask(request):
    if request.method=='POST':
        tasks.append(request.POST['task'])
        return redirect('view-task')
    else:
        return render(request,"taskapp/addtask.html")