from django.contrib import admin
from .models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email_address', 'hire_date', 'phone')
    list_display_links = ('id', 'name', 'email_address')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Realtor, RealtorAdmin)

