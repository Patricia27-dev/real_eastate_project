from django.contrib import admin
from .models import Listing


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display= ('id' , 'title', 'is_published', 'city', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title', 'realtor')
    list_filter = ('realtor',)
    list_editable = ('is_published', 'price')
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 20

admin.site.register(Listing, ListingAdmin)

