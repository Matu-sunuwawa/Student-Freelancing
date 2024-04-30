from django.contrib import admin
from .models import Customer,ShoppingCart,Product,ProductCategory,Variation,Payment,Order,OrderItem,Discount,CustomerAddress

# Register your models here.
admin.site.register(Customer)
admin.site.register(ShoppingCart)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Variation)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Discount)
admin.site.register(CustomerAddress)