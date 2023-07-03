from django.contrib import admin
from .models import *

# this section shows categories in admin site
# shall i add category?
# no

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
