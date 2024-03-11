from django.contrib import admin
from django.utils.html import format_html
from .models import Customer,Category,Product,Order,OrderDetail


class customerList(admin.ModelAdmin):
    list_display        = ['first_name','last_name','province','district','village','email','phone','password','note','created_at']
    search_fields       = ['first_name','last_name','email','phone','province','district']

class categoryList(admin.ModelAdmin):
    list_display = ['name']

class productList(admin.ModelAdmin):
    list_display        = ['show_image','product_no','category_id','product_name','quantity','base_price','sale_price','description','status','created_at']
    list_filter         = ['status']
    search_fields       = ['product_no','category_id','product_name']
    prepopulated_fields = {'slug':['product_name']}
    actions             = ('update_status',)
    # readonly_fields     = ['product_no']

    def update_status(self, request, queryset):
        for obj in queryset:
            obj.status = not obj.status #Toggle status
            obj.save()
    update_status.short_description = 'Update Status'

class orderList(admin.ModelAdmin):
    list_display  = ['bill_no','product_no','customer_id','quantity','sale_price','total_price','status_button','created_at']
    list_filter   = ['payment_status']
    search_fields = ['bill_no','product_no','customer_id']
    actions       = ('confirm_payment',)

    def confirm_payment(self,request,queryset):
        queryset.update(payment_status = 1)
        self.message_user(request,'Payment has been updated.')
    confirm_payment.short_description='Confirm Payment'    

class orderdetailList(admin.ModelAdmin):
    list_display  = ['bill_no','customer_id','product_no','quantity','sale_price','created_at']
    search_fields = ['product_no','category_id','product_name']

admin.site.register(Category,categoryList)
admin.site.register(Product,productList)
admin.site.register(Customer,customerList)
admin.site.register(Order,orderList)
admin.site.register(OrderDetail,orderdetailList)