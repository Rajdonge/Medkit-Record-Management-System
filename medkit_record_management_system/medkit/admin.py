from django.contrib import admin
from .models import Information

# Register your models here.


@admin.register(Information)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'medicine_name', 'expiry_date', 'quantity',
                    'marked_price', 'discount', 'company', 'dealer')
    

admin.site.site_header = "Medkit Record Management System"


