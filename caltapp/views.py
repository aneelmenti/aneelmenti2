from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'input.html')
def calculate(request):
    x=int(request.GET["t1"])
    y=int(request.GET["t2"])
    op_type=request.GET["op"]
    z=0
    if op_type=="add":
        z=x+y
    elif op_type=="sub":
        z=x-y
    elif op_type=="mul":
        z=x*y
    else:
        z=x/y
    res=HttpResponse("the result is:"+str(z))
    return res
