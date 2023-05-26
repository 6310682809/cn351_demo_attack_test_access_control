from django.contrib import admin
from user.models import UserInfo
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user", "role")

admin.site.register(UserInfo, UserInfoAdmin)