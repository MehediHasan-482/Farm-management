from itertools import product
from multiprocessing import Value
from optparse import Values
from wsgiref import validate
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import cow,cart
from .models import Contact
from .models import protfolio
# from django.views import View

#@login_required(login_url='login')

def index (request):
    return render(request,"home/index.html" , context={'page' : 'django project'})

def signup(request):

    if request.method != "POST":
        return render(request,"home/signup.html", context={'page' : 'django project'})
    username = request.POST.get('username')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    pass1 = request.POST.get('pass1')
    pass2 = request.POST.get('pass2')

    if pass1 != pass2:
        return HttpResponse("Your password and confirm password are not same!!")
    myuser= User.objects.create_user(username,email,pass1)
    myuser.save()
    return redirect('signin')

def signin(request):
    if request.method=='POST':
        username =request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(request, username=username, password=pass1)
        if user is None:
            return HttpResponse ("Username or password is incorrect!!!")


        login(request, user)
        return redirect('home')
    return render(request,"home/signin.html", context={'page' : 'django project'})

def home (request):
    cows = cow.objects.all()
    return render(request,"home/home.html" ,{'cows': cows})

def logout (request):
    #logout(request)
    #return redirect('signin')
    return render(request,"home/signin.html") 

def about (request):
    context = {'page':'about'}
    return render(request, "home/about.html", context)    


def contact (request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        mehedi = Contact(name=name, email=email, phone=phone, content=content)
        mehedi.save()
    context = {'page':'contact'}
    return render(request,"home/contact.html", context)  

def portfolio (request): 
    identy = protfolio.objects.all()
    return render(request,"home/portfolio.html",{'identy' : identy})  

def service (request): 
    cows = cow.objects.all()
    return render(request,"home/service.html" ,{'cows': cows})

# class Service(View):
#     def get(self,request):
#         cows = cow.objects.all()
#         return render(request,"home/service.html" ,{'cows': cows})
#     def post(self,request):
#         if request.method=='POST':
#             product=request.POST.get('product')
#             cart=request.session.get('cart')
#             if cart:
#                 quantity = cart.get('product')
#                 if quantity:
#                     cart[product] = quantity+1
#             else:
#                 cart = {}
#                 cart[product]= 1

#             request.session['cart'] = cart 
#             print('cart', request.session['cart'])
#             return redirect('service')


def add_to_cart(request):
    if request.method=='POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        product = request.POST.get('product')
        hasan = cart(product_name=name,phone=phone,product_id=product)
        hasan.save()
    context = {'page':'add_to_cart'}
    return render(request,"home/add_to_cart.html", context)  

    #return redirect('service')
    # context = {'page': add_to_cart}
    #return redirect('home')
    #return render(request,"home/add_to_cart.html", context)  



 
                             