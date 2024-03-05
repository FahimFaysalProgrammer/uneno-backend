from django.contrib import admin
from . models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','mobile_no', 'image']
    
    def first_name(self, object):
        return object.user.first_name
    
    def last_name(self, object):
        return object.user.last_name
    
admin.site.register(Customer, CustomerAdmin)