from django.contrib import admin
from .models import *

# Register your models here.


class RestaurantModelAdmin(admin.ModelAdmin):
    list_filter = ("name", "location", "description", "rating")
    list_display = ("name", "location", "description", "rating","res_image" ,"createdAt")
    search_fields = ("name", "rating","location")


class CategoryModelAdmin(admin.ModelAdmin):
    
    list_display = ("name","createdAt")
    search_fields = ("name","")


class ItemModelAdmin(admin.ModelAdmin):
    list_filter = ("name", "description", "rating","price")
    list_display = ("name", "price", "description", "rating", "res_image","createdAt")
    search_fields = ("name", "rating", "price")
   

admin.site.register(Restaurant, RestaurantModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Item, ItemModelAdmin)

### admin page header and title changed
admin.site.site_title = 'Just Eat Admin'
admin.site.site_header = 'Just Eat Admin'