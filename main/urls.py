from django.urls import path
from .views import *
from   . import views 
urlpatterns=[
    path('',Index),
    # path('shop_cart/',Shop_cart),
    path('contact2/',Contact2),
    path('blog/',Blog),
    # path('single/',Single),
    # path('contact/',Contact),
    path('html/',Html),
    path('product/<int:pk>/', views.ContactDetailView.as_view(),name='product' ),
    # path('order/'include('order.urls ')), 
     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('message/',Send),  
    path('yubor/',Go),
    path('list/',List),
    path('about_us/',About_us),
    path('dostavka/',Dostavka),
    path('возврат/',Возврат),
    path('oбразы/',Образы),
    path('звезды/',Звезды),
    path('oтзывы/',Отзывы),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('cart/', views.cart_view, name='cart'),  # Bu joyga e'tibor bering
    path('cart/increase/<int:order_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:order_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.contact_list_by_category, name='contact_list_by_category'),
    
    path('admin-orders/', views.zakazlar_admin, name='admin_orders'),
    path('delete-order/<int:zakaz_id>/', views.delete_order, name='delete_order'),


]
