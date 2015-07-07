from django.contrib import admin
from group4.models import *
# Register your models here.


class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('id','account_id','user','disease','dateCommit')

admin.site.register(WithdrawCure, WithdrawAdmin)
admin.site.register(WithdrawStudy)
admin.site.register(Father)
admin.site.register(Mother)
admin.site.register(Spouse)
admin.site.register(Child)
admin.site.register(EditPresident)
admin.site.register(DataFromWeb)
admin.site.register(Olddate)