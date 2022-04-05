from warnings import catch_warnings
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")
        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

def second_page(request):
    user = get_object_or_404(User,id = request.user.id)
    return render(request, "custom_pages/second_page.html",{'user': user})

        
def second_page_post(request):

    user = get_object_or_404(User,id = request.user.id)
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        email = request.POST['email']
        password = request.POST.get('password')


       
        user.first_name = fname
        user.last_name = lname
        user.username = username
        user.email = email
        user.password = password
        user.save()

        return render(request, "custom_pages/second_page.html",{'user': user})

 
    

    
   

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
