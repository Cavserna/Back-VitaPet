from django.urls import path
from shop_app.api.views import (ProductList, ProductDetail, CategoryList, 
                                CategoryDetail, OrderList, OrderDetail) 

urlpatterns = [
    path('product/', ProductList.as_view(), name='product-list' ),
    path('product/<int:pk>', ProductDetail.as_view(), name='product-detail'),
    
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>', CategoryDetail.as_view(), name='category-detail'),
    
    path('order/', OrderList.as_view(), name='order-list'),
    path('order/<int:pk>', OrderDetail.as_view(), name='order-detail'),
    
    
    
    
]
