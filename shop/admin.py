from django.contrib import admin
from . models import *


# Register your models here.
class catagdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
admin.site.register(categ,catagdmin)



class prodAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','img']
    list_editable=['price','stock','img']
    prepopulated_fields ={'slug':('name',)}
admin.site.register(products,prodAdmin)

