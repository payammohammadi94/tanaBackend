from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone','referer']
    list_filter = ['user','phone']
    
admin.site.register(Profile,ProfileAdmin)