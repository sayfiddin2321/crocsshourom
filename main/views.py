from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.views.generic import DetailView
from .models import Contact
def Html(request):
     context={
          'xatolik':Xatolik.objects.first(),
          'category':Category.objects.all(),
          
          
     }
     return render(request,'404.html',context)
def Index(request):
    context={
        'index_home':Index_Home.objects.all(),
        'card':Contact.objects.all(),
        'card1':Contact.objects.all(),
        'news':News.objects.all(),
        'small_card':Small.objects.all(),
        'categories':Category.objects.all(),
        'order':OrderItem.objects.all(),
        'contact':Contact.objects.all(),
        'imagesrk':Imagesrk.objects.first(),
        
    }
    
    return render(request,'index.html',context)

        
        
class ContactDetailView(DetailView):
    template_name='single-product.html'
    model=Contact
    context_object_name='product'
    






def Contact2(request):
    context={
        'categories':Category.objects.all(),
    }
    return render(request,"contact.html",context)


def Blog(request):
    context={
        'blognew':BlogNew.objects.all(),
        'categories':Category.objects.all(),
    }
    return render(request,"blog.html",context)


from django.shortcuts import render, get_object_or_404, redirect
from .models import  Order, OrderItem

def add_to_cart(request, product_id):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()

    product = get_object_or_404(Contact, id=product_id)
    order, created = Order.objects.get_or_create(
        session_key=session_key,
        is_ordered=False
    )

    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect('cart_detail')

def cart_detail(request):
  
    session_key = request.session.session_key
    if not session_key:
        request.session.create()

    order = Order.objects.filter(session_key=session_key, is_ordered=False).first()
    if not order:
        items = []
        total = 0
    else:
        items = order.items.all()
        total = order.get_total()

    return render(request, 'shop-card.html', {'items': items, 'total': total,"order":OrderItem.objects.all(),"categories":Category.objects.all()})

def checkout(request):
    session_key = request.session.session_key
    order = Order.objects.filter(session_key=session_key, is_ordered=False).first()
    if order:
        order.is_ordered = True
        order.save()
    return redirect('cart_detail')
from .models import  Message

def Send(request):
    if request.method == 'POST':
        name =request.POST['name']
        email = request.POST['email']
        mavzu = request.POST['mavzu']
        text = request.POST['text']
        
        
        Message.objects.create(name=name, email=email,mavzu=mavzu,text=text)

        # Bu yerda SMS jo‘natish funksiyasi bo‘lishi mumkin (tashqi servis orqali)
        return redirect('/message/')

    return render(request, 'contact.html')
def Go(request):
    if request.method == 'POST':
        shaxar =request.POST['shaxar']
        yashash = request.POST['yashash']
        name = request.POST['name']
        tel= request.POST['tel']
        razmer=request.POST['razmer']
        Yubor.objects.create(shaxar=shaxar, yashash=yashash,name=name,tel=tel,razmer=razmer)

        # Bu yerda SMS jo‘natish funksiyasi bo‘lishi mumkin (tashqi servis orqali)
        return redirect('/')

    return render(request, 'index.html')


def List(request):
    context={
        'categories':object.all(),
    }
    return render (request,'product_list.html',context)




# def AddToCart(request):
#     pr = request.GET.get('product')
#     prod = Product.objects.get(id=pr)
#     savat = Shop.objects.filter(client=request.user, status=0)
#     if len(savat) == 0:
#         svt = Shop.objects.create(client=request.user)
#     else:
#         svt = savat[0]
#     new_p = new_price(prod)
#     svt.total += new_p
#     my_items = ShopItems.objects.filter(shop__client=request.user, shop__status=0, product=prod)
#     if len(my_items) == 0:
#         ShopItems.objects.create(shop=svt, product=prod, quantity=1, totalPay=new_p)
#     else:
#         current_item = my_items[0]
#         current_item.quantity += 1
#         current_item.totalPay += new_p
#         current_item.save()

#     svt.save()
   
#     messages.success(request, f'Savatchaga <strong>{prod.name}</strong> qo`shildi.')
    
    
   
    return redirect('/')
from django.shortcuts import get_object_or_404, redirect
from .models import Order  # yoki CartItem

def delete_cart_item(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id)
    item.delete()
    return redirect('cart')  # yoki redirect('/cart/')
    item = get_object_or_404(OrderItem, id=item_id)
    item.delete()
    return redirect('cart_detail')  # yoki o‘zingizning cart sahifangiz nomi


# Narx (masalan: 10000 so‘m har bir mahsulot uchun)
from django.shortcuts import redirect, get_object_or_404
from .models import OrderItem  # yoki CartItem, agar model nomi boshqacha bo‘lsa
from django.views.decorators.http import require_POST

@require_POST
def increase_quantity(request, order_id):
    order = get_object_or_404(OrderItem, id=order_id)
    order.quantity += 1
    order.save()
    return redirect('cart')  # yoki kerakli sahifa nomi

@require_POST
def decrease_quantity(request, order_id):
    order = get_object_or_404(OrderItem, id=order_id)
    if order.quantity > 1:
        order.quantity -= 1
        order.save()
    return redirect('cart')  # yoki kerakli sahifa nomi


def cart_view(request):
    orders = OrderItem.objects.filter(user=request.user)  # yoki mos filter
    return render(request, 'cart.html', {'orders': orders})
# views.py

from django.shortcuts import render

from .models import Category, Contact

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def contact_list_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    contacts = Contact.objects.filter(category=category)
    categories=Category.objects.all()
    categ=Category.objects.all()
    return render(request, 'product_list.html', {
        'category': category,
        'contact': contacts,
        'categories':categories,
    })
    
def About_us(request):
    context={
        'about_2':About_2.objects.first(),
        'categories':Category.objects.all(),
        
    }
    return render(request,'about_us.html',context)

def Dostavka (request):
    context = {
        'dostavka_2':Dostavka_2.objects.first(),
        'categories':Category.objects.all(),
    }
    return render(request,'dostavka.html',context)
def Возврат(request):
    context = {
        'vozvarat_2':Vozvarat_2.objects.first(),
        'categories':Category.objects.all(),
        
    }
    return render(request,'возврат.html',context)
def Образы(request):
    context={
        'imagess':Imagess.objects.first(),
        'categories':Category.objects.all(),
        
    }
    return render(request,'oбразы.html',context)

def Звезды(request):
    context={
        'zvezdi':Zvezdi.objects.all(),
        'categories':Category.objects.all(),
        
    }
    return render(request,'звезды.html',context)

def Отзывы(request):
    context={
        'reviews':Review.objects.all(),
        'categories':Category.objects.all(),
        
    }
    return render(request,'oтзывы.html',context)
def Base(request):
    context={
        'categories':Category.objects.all()
    }
    return render(request,'base.html',context)