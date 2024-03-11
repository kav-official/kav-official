from django.urls import path,re_path
from django.contrib import admin
from . import views

admin.site.site_header = 'SHOPING MORE'
admin.site.site_title = 'Shoping More'
admin.site.index_title = 'Shoping More Administration'

urlpatterns = [
    path('',views.index, name='index'),
    # Production
    path('get/product/', views.getAllProduct,name='get-product'),
    path('get/product/id/<str:pk>',views.getOneProduct,name='get-product-id'),
    # Order
    path('get/order/',views.getAllOrder, name='get-order'),
    path('get/order/bill/<str:bill>',views.getOneOrder, name='get-order-id'),
    path('get/order-detail',views.getOrderDetail,name='get-order-detail'),
    path('get/order-detail/bill/<str:bill>',views.getOneOrderDetail,name='get-order-detail-id'),
]