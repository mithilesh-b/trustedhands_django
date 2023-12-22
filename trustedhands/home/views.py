from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        # "variable1": "Hello Coder",
        # "variable2": "Hello World!"
    }

    # messages.success(request, "this is a text message")

    return render(request, 'index.html', context)
   # return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is service page")

def donate(request):
    return render(request, 'payment.html')

def contact(request):
   
    if request.method == "POST":
       print("hiiii")
       sname = request.POST.get('name')
       semail = request.POST.get('email')
       sphone = request.POST.get('phone')
       sdesc = request.POST.get('desc')

       print(sname, semail, sphone, sdesc)
       print("Data, {}!".format(sname))
       print("Data, {}!".format(semail))
       


       contact = Contact(name=sname, email=semail, phone=sphone, desc=sdesc, date=datetime.today())
       contact.save()
       messages.success(request, 'Thank you! Your message has been sent')

    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")



