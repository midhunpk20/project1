from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def home(request):
    data =ExampleModel.objects.all()

    return render(request,'home.html',{'data':data})

    

def stock(request):
    if request.method =='POST':
        a =request.POST.get("s_name")
        b =request.POST.get("s_description")
        c =request.POST.get("s_category")
        d =request.POST.get("s_stock_quantity")
        e =request.POST.get("s_image")


        ExampleModel.objects.create(

            name =a,
            description =b,
            category =c,
            stock_quantity =d,
            image =e,
        )

        return redirect("home_link")

    return render(request,'stock.html')

def view(request,id):
    data = ExampleModel.objects.get(id=id)

    return render(request,'view.html',{'data':data})



def update(request,id):
    data= ExampleModel.objects.get(id=id)

    if request.method=="POST":
        a =request.POST.get("s_name")
        b =request.POST.get("s_description")
        c =request.POST.get("s_category")
        d =request.POST.get("s_stock_quantity")
        e =request.POST.get("s_image")

        if a:
            data.name =a
        if b:
            data.description =b   
        if c:
            data.category =c
        if d:
            data.stock_quantity =d
        if e:
            data.image =e    

        data.save()     

        return redirect("home_link")                              


    return render(request,'update.html',{'data':data})   


def user_delete(request,id):
    dele =ExampleModel.objects.get(id=id)
    dele.delete()

    return redirect("home_link")

        