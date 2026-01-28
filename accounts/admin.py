from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,UserProfile
from django.utils.html import format_html
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email','username','first_name','last_name','last_login','date_joined','is_active','is_staff',)
    list_display_links = ('email','first_name','last_name',)
    readonly_fields = ('last_login','date_joined',)
    ordering = ('-date_joined',)
    search_fields = ('email', 'username', 'first_name', 'last_name', 'phone_number')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        if object.profile_picture:
            return format_html('<img src="{}" width="50" style="border-radius: 50px;" />', object.profile_picture.url)
        return 'No Image'
    thumbnail.short_description = 'Profile Picture'

    list_display = ('thumbnail','user','city','state','country')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'city', 'state', 'country')

admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
