from ast import And
from lib2to3.pgen2.token import EQUAL
from urllib import response
from warnings import catch_warnings
from xmlrpc.client import DateTime
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from pymysql import NULL
from .models import Customer
from food.models import Restaurant,Item,Order
import datetime
from django.db.models import Q

# Create your views here.

def home(request):

    qstr = request.GET.get('searchFor', '')
    if qstr == '':
        resrtaurents = Restaurant.objects.all()
    else:
        # resrtaurents = Restaurant.objects.filter(food_restaurant__name__icontains=qstr)
        resrtaurents = Restaurant.objects.filter(Q(name__icontains=qstr) | Q(food_restaurant__name__icontains=qstr))

    return render(request, "authentication/index.html",{'resrtaurents':resrtaurents, 'qstr':qstr})

def food_items(request,id,food_id=''):

    items = Item.objects.filter(restaurant_id_id = id)
    res_message = ''

    if food_id != '' and request.session.get('customer_id') is not None:
       
        food = Item.objects.get(id = food_id)
        order = Order(price=food.price,is_added_to_cart	= True,food_id_id = food_id,restaurant_id_id = id,cart_added_date= datetime.datetime.now(),customer_id= request.session.get('customer_id')) 
        order.save()
    else:
        res_message = 'To add item in the Cart , Please Login'


    return render(request, "custom_pages/food_items.html",{'items':items,'res_message': res_message})

def signup(request):

    responseMessage = ''
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email'].lower()
        
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        full_name = fname + ' ' +lname

        if email is not None :
            
            try:
                customer =  Customer.objects.get(email=email)
            except:
                customer = None
               

            if customer is not None :
                responseMessage = 'Email Already Registered.Please Try with Another Email'
                return render(request, 'authentication/signup.html',{'response':responseMessage})
            else:
                if pass1 != pass2:
                    responseMessage = "Password Don't Match"
                    return render(request, "authentication/signup.html",{'response':responseMessage})
                if username is not None and fname is not None and lname is not None and email is not None and pass1 is not None:
                    Customer.objects.create(first_Name= fname,last_name= lname,email=email,user_name=username,password=pass1,full_name=full_name)
                    return render(request,"authentication/signin.html")
                else:
                    return render(request, "authentication/signup.html",{'response':responseMessage})
                
        else:
            return render(request, "authentication/signup.html",{'response':responseMessage})
    else:
         return render(request, "authentication/signup.html",{'response':responseMessage})


def signin(request):
    response_message = ''

    if request.method == 'POST':

        customer =  Customer.objects.get(user_name=request.POST['username'])
        
        if customer is not None:
            if customer.password == request.POST['password']:
                request.session['customer_id'] = customer.id
                response_message = 'User Authenticated Successfully'
                return render(request, "authentication/index.html", {'customer': customer, 'response': response_message})  
                
            else:
                response_message = "Provided password is Wrong.Please try with correct Password"
                return render(request, "authentication/signin.html",{'response': response_message})
        else:
            return render(request, "authentication/index.html", {'customer': customer, 'response': response_message})  
    return render(request, "authentication/signin.html",{'response': response_message})
    
def signout(request):
    logout(request)
    #del request.session['customer_id']
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

def second_page(request):
    customer = Customer.objects.get(id = request.session.get('customer_id'))

    if request.method == 'POST':
      
        customer.first_Name = request.POST['first_name'].strip()
        customer.last_name = request.POST['last_name'].strip()
        customer.user_name = request.POST['username'].strip()
        customer.email = request.POST['email'].strip()
        customer.full_name = request.POST['first_name'].strip() + ' ' +request.POST['last_name'].strip()
        customer.save()
        del request.session['customer_id']
        request.session['customer_id'] = customer.id
        return render(request, "custom_pages/second_page.html",{'user': customer})

       
    else:
        return render(request, "custom_pages/second_page.html",{'user': customer})

def forgot_password(request):
    responseMessage  = ''

    if request.method == 'POST':
        email = request.POST['email'].strip()

        customer = Customer.objects.get(email = email)

        if customer is not None:
            return render(request, "authentication/password_reset.html",{'customer': customer}) 
        else:
            
            responseMessage = 'User not Found with the Provided Email Address.'
            return render(request, "authentication/forgot_password.html",{'message': responseMessage})
            
    else:
        return render(request, "authentication/forgot_password.html")
  
def password_reset(request):

    responseMessage  = ''

    if request.method == 'POST':
        password_new = request.POST['new_password'].strip()
        new_password_confirm = request.POST['new_password_confirm'].strip()
        email = request.POST['email'].lower()
        
        if password_new == new_password_confirm:
            customer = Customer.objects.get(email = email)
            customer.password = password_new
            customer.save()
            responseMessage = "Password reset SuccessFully.Please Login Again"
            return render (request, "authentication/signin.html",{'response': responseMessage})
        else:
            responseMessage = "Both password Don't Match"
            return render (request, 'authentication/password_reset.html',{'response': responseMessage})
    else:
        return render(request,'authentication/password_reset.html',{'response': responseMessage})

def about_us(request):

    return render(request, "custom_pages/aboutUs.html")

def gallery(request):
    
    return render(request, "custom_pages/gallery.html")

def contact_us(request):

    responseMessage = ""
    
    if request.method == 'POST':
        username = request.POST['userName']
        email = request.POST['email']
        message = request.POST['message']
        admin_email = "darkthrone742@gmail.com"

        try:
            send_mail('Mail From Contact Us Page',message,email,[settings.DEFAULT_FROM_EMAIL],fail_silently=False,)
            responseMessage = "Email Send Successfully."
            
        except:

            responseMessage =  "Email Not send due to technical Problems."

            return render(request, "custom_pages/contactUs.html",{'responseMessage': responseMessage})
  
    return render(request, "custom_pages/contactUs.html",{'responseMessage': responseMessage})
