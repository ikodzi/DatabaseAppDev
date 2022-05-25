from django.contrib import admin
from . models import callBack
# Register your models here.
admin.site.site_header = 'Camel Admin'


# class ClotheStoreAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created')
#     list_filter = ('title', 'created')
#
# admin.site.register(clotheStore, ClotheStoreAdmin)
admin.site.register(callBack)

