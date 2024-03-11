from django.db import models
from django.utils.html import format_html

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

class Product(models.Model):
    product_no    = models.CharField(max_length=20,unique=True)
    category_id   = models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE)
    product_name  = models.CharField(max_length=200,unique=True)
    slug          = models.SlugField(max_length=200,unique=True)
    product_image = models.FileField(upload_to='upload', null=True,blank=True)
    quantity      = models.IntegerField(default=1)
    base_price    = models.IntegerField()
    sale_price    = models.IntegerField()
    description   = models.TextField(unique=True)
    status        = models.IntegerField(default=1)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        ordering            = ['-created_at']
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.product_name
    
    def show_image(self):
        if self.product_image:
             return format_html('<img src="'+ self.product_image.url +'" height="60px">')
        return ''
    show_image.allow_tags = True

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    province   = models.IntegerField()
    district   = models.IntegerField()
    village    = models.CharField(max_length=200)
    email      = models.EmailField(max_length=100)
    phone      = models.CharField(max_length=30,help_text='Enter phone number')
    password   = models.CharField(max_length=100,)
    note       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering            = ['-created_at']
        verbose_name_plural = 'Customer'

    def __str__(self):
        return self.first_name

class Order(models.Model):
    bill_no        = models.CharField(max_length=10)
    product_no     = models.ForeignKey(Product,null=True,blank=True,on_delete=models.CASCADE)
    customer_id    = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE)
    quantity       = models.IntegerField()
    sale_price     = models.IntegerField()
    total_price    = models.IntegerField()
    payment_status = models.IntegerField(default=0)
    created_at     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering           = ['-bill_no']
        verbose_name_plural = 'Order'

    def __str__(self):
        return self.bill_no
    
    def status_button(self):
        if self.payment_status == 0:
            return format_html('<a style="background-color: yellow;padding:5px;" href="#">Pending</a>')
        elif self.payment_status == 1:
            return format_html('<a style="background-color: green;color:#ffffff;padding:5px;" href="#">Paided</a>')
    status_button.allow_tags = True
    status_button.short_description = "Pay status"

class OrderDetail(models.Model):
    bill_no     = models.CharField(max_length=20)
    customer_id = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE)
    product_no  = models.ForeignKey(Product,null=True,blank=True,on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=1)
    sale_price  = models.IntegerField()
    created_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering            = ['-bill_no']
        verbose_name_plural = 'Order Detail'

    def __str__(self):
        self.bill_no