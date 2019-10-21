from django.contrib import admin
from .models import Collection, Style, Item, CartItem, Order


# Register your models here.
admin.site.register(Collection)
admin.site.register(Style)
admin.site.register(Item)
admin.site.register(CartItem)
admin.site.register(Order)