
from django.contrib import admin
from group1.models import Category, Document, Personal, Document_modify


class documentAdmin(admin.ModelAdmin):
    search_fields = ('name','number',)
    list_filter = ['name']

admin.site.register(Category)
admin.site.register(Document, documentAdmin)
admin.site.register(Personal)
admin.site.register(Document_modify)
