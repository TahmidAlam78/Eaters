from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('home', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('second-page', views.second_page, name="second-page"),
    # path('second-page-post', views.second_page_post, name="second-page-post"),
    path('about-us', views.about_us, name="aboutus"),
    path('gallery', views.gallery, name="gallery"),
    path('contact-us', views.contact_us, name="contactus"),
    path('forgot_password', views.forgot_password, name="forgot_password"),
    path('password_reset', views.password_reset, name="password_reset"),
    path('restaurents/<int:id>', views.food_items, name = 'food_items'),
    path('add_food_items/<int:restaurant_id>/<int:food_id>', views.add_food_items, name = 'add_food_items'),
    path('checkout', views.checkout, name = 'checkout'),
    path('add-voucher', views.add_voucher, name = 'add_voucher'),
    
]