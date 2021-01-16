from django.contrib import admin
from .models import Listing
# Register your models here.
class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'dollar_price', 'list_date', 'realtor') #display dollar amount rather than price
    list_display_links = ('id', 'title') #  by clicking in the id or tittle it will open the obeject to modify
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

    def dollar_price(self, obj): #Used to render a $ in front of each price, and add commas in for readability
        return "${:,}".format(obj.price)
    dollar_price.short_description = 'price'
admin.site.register(Listing, ListingsAdmin)

