from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('second-page', views.second_page, name="second-page"),
    path('second-page-post', views.second_page_post, name="second-page-post"),
    path('about-us', views.about_us, name="aboutus"),
    path('gallery', views.gallery, name="gallery"),
    path('contact-us', views.contact_us, name="contactus"),

]