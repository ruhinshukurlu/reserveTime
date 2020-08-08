from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import *
from restaurant.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','company_name','city_location','province_location','country_location',)
    
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title','price', 'description','menu_type',)
    
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['owner','photo','photo_url','photo_type']

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['company','user','text','comment_img','commented_at']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['company','size','table_place']

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['free_time','reserved']

@admin.register(TableDate)
class TableDateAdmin(admin.ModelAdmin):
    list_display = ['date']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['company','user','reserved_time','table_id']

@admin.register(Portion)
class PortionAdmin(admin.ModelAdmin):
    list_display = ['menu_id','portion_count']
    
