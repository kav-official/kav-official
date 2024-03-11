import os
from dotenv import load_dotenv
load_dotenv()
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import productSerializer,categorySerializer,orderSerializer,orderDetailSerializer
from .models import Product,Category,Customer,Order,OrderDetail

SITE_NAME = os.getenv('SITE_NAME')
def index(request):
    return render(request,'index.html',{'SITE_NAME':SITE_NAME})

@api_view(['GET'])
def getAllProduct(request):
    product = Product.objects.all()
    if product:
        serializer = productSerializer(product, many=True)
        return Response(serializer.data)
    return Response({'Message':'Empty Data'})

@api_view(['GET'])
def getOneProduct(request,pk):
    datas = get_object_or_404(Product,product_no=pk)
    if datas:
        serializer = productSerializer(datas,many=False)
        return Response(serializer.data)
    return Response({'Message:','not faund this product no'})

@api_view(['GET'])
def getAllOrder(request):
    datas      = Order.objects.all()
    serializer = orderSerializer(datas,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOneOrder(request,bill):
    datas      = get_object_or_404(Order,bill_no=bill)
    serializer = orderSerializer(datas,read_only=False)
    return Response(serializer.data)

@api_view(['GET'])
def getOrderDetail(request):
    datas      = OrderDetail.objects.all()
    serializer = orderDetailSerializer(datas,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOneOrderDetail(request,bill):
    datas      = get_object_or_404(OrderDetail,bill_no=bill)
    serializer = orderDetailSerializer(datas,read_only=False)
    return Response(serializer.data)