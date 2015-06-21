from django.contrib import admin
from login.models import *

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname_en', 'lastname_en')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Officer)