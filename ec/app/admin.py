from django.contrib import admin
from .models import Product,Customer,Cart,Payment,OrderPlaced,Wishlist
# Register your models here.
from django.urls import reverse
from django.utils.html import format_html 


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','state','zipcode']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','products','quantity']
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html('<a href = {}>{}</a>',link,obj.product.title)


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status','payment']


@admin.register(Wishlist)
class WishListModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','products']
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html('<a href = {}>{}</a>',link,obj.product.title)

# admin.site.register(models.Product,ProductModelAdmin)

admin.site.site_header = 'Ephraim Milk Processing Group'
admin.site.site_title = 'Ephraim Milk Processing Group'
admin.site.site_index_title = 'Welcome to Ephraim Milk Processing Group'