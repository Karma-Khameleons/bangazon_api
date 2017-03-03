from django.contrib import admin
from api.models import *

admin.site.register(customer.Customer)
admin.site.register(product_type.ProductType)
admin.site.register(product.Product)
admin.site.register(payment_type.PaymentType)
admin.site.register(customer_order.CustomerOrder)
admin.site.register(line_item.LineItem)
