from rest_framework.serializers import ModelSerializer
from .models import Product,Category,Customer,Order,OrderDetail

class categorySerializer(ModelSerializer):
    class Meta:
        model  = Category
        fields = ['id','name']

class productSerializer(ModelSerializer):
    class Meta:
        category_id = categorySerializer(read_only = True)
        model       = Product
        fields      = ['id','category_id','product_no','product_name','product_image','slug','quantity','base_price','sale_price','description','status','created_at','updated_at']

class customerSerializer(ModelSerializer):
    class Meta:
        model  = Customer
        fields = ['first_name','last_name','province','district','village','email','phone','password','note','created_at']

class orderSerializer(ModelSerializer):
    class Meta:
        customer_id = customerSerializer(read_only=True)
        model       = Order
        fields      = ['bill_no','product_no','customer_id','quantity','sale_price','total_price','payment_status','created_at']

class orderDetailSerializer(ModelSerializer):
    class Meta:
        customer_id = customerSerializer(read_only=True)
        model       = OrderDetail
        fields      = ['bill_no','customer_id','product_no','quantity','sale_price','created_at']