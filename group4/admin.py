from django.contrib import admin
from group4.models import *
# Register your models here.


class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('id','account_id','disease','dateCommit')


admin.site.register(Withdraw, WithdrawAdmin)
admin.site.register(Family)
admin.site.register(Spouse)
admin.site.register(Child)
admin.site.register(DataFromWeb)
admin.site.register(Olddate)