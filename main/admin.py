from django.contrib import admin
from .models import *
from .models import Message,Yubor
# Register your models here.

admin.site.register(Index_Home)
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(BlogNew)
admin.site.register(Xatolik)
admin.site.register(Small)
admin.site.register([Order,OrderItem])
admin.site.register(Message)
admin.site.register(Yubor)
admin.site.register(Category)
admin.site.register(About_2)
admin.site.register(Dostavka_2)
admin.site.register(Vozvarat_2)
admin.site.register(Imagess)
admin.site.register(Zvezdi)
admin.site.register(Review)
admin.site.register(Imagesrk)
class MessageInline(admin.TabularInline):
    model = Message
    extra = 1
    