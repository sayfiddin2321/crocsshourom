from django.db import models

# Create your models here.


class Index_Home(models.Model):
    background_img = models.ImageField(upload_to='media/')
  
        
    
from django.db import models


# Kategoriya modeli kerak bo‘lishi mumkin
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    title = models.CharField(max_length=100)
    discount_price = models.IntegerField()
    price = models.IntegerField()

    img = models.ImageField(upload_to='media/')
    img1 = models.ImageField(upload_to='media/')
    img2 = models.ImageField(upload_to='media/',null=True, blank=True )
    img3 = models.ImageField(upload_to='media/',null=True, blank=True)
    img4 = models.ImageField(upload_to='media/',null=True, blank=True)
    img5 = models.ImageField(upload_to='media/',null=True, blank=True)
    
    quantity = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    @property
    def discount_percent(self):
        try:
            if self.price and self.discount_price and self.price > 0:
                return round((self.price - self.discount_price) / self.price * 100)
            return 0
        except:
            return 0

    def __str__(self):
        return self.title

    @property
    def total_price(self):
        """
        E'tibor bering: Bu modeldagi `quantity` — mahsulot ombordagi mavjud soni.
        Savatcha (OrderItem) uchun emas!
        """
        return self.quantity * (self.discount_price if self.discount_price < self.price else self.price)


class News(models.Model):
    title = models.CharField(max_length=100)
    sana = models.CharField(max_length=120)
    text = models.TextField()
    img = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title


class BlogNew(models.Model):
    title = models.CharField(max_length=100)
    sana = models.DateField()
    img = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title


class Xatolik(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)


class Small(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/')


class Order(models.Model):
    session_key = models.CharField(max_length=40, null=True, blank=True)
    is_ordered = models.BooleanField(default=False)

    def get_total(self):
        """
        Har bir OrderItem dan to‘g‘ri narxni olamiz — agar chegirma bor bo‘lsa, shuni hisoblaydi.
        """
        return sum(item.get_total() for item in self.items.all())

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Contact, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total(self):
        """
        Chegirmali narxni hisoblaydi agar mavjud bo‘lsa
        """
        if self.product.discount_price and self.product.discount_price < self.product.price:
            return self.quantity * self.product.discount_price
        return self.quantity * self.product.price

    @property
    def total_price(self):
        return self.get_total()

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"





class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mavzu=models.CharField(max_length=200)
    text=models.TextField()
    def __str__(self):
        return self.name


class Yubor(models.Model):
    shaxar = models.CharField(max_length=200)
    yashash = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=20)  # Integer emas, chunki raqamlar 0 bilan boshlanishi mumkin
    razmer = models.CharField(max_length=50, null=True, blank=True)  # Optional

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='yubor_info')

    def __str__(self):
        return f"{self.name} - {self.shaxar}"


    
class About_2(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(upload_to='meida/')

class Dostavka_2(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(upload_to='meida/')
    
    
    
class Vozvarat_2(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(upload_to='meida/')
    
    
class Imagess(models.Model):
    img_1 = models.ImageField(upload_to='meida/')
    img_2 = models.ImageField(upload_to='meida/')
    img_3 = models.ImageField(upload_to='meida/')
    img_4 = models.ImageField(upload_to='meida/')
    
class Zvezdi(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='meida/')
    
class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ismi")
    avatar = models.ImageField(upload_to='media/', verbose_name="Avatar rasmi", blank=True, null=True)
    rating = models.PositiveSmallIntegerField(verbose_name="Bahosi (1-5)", default=5)
    text = models.TextField(verbose_name="Izoh matni")
    
    
class Imagesrk(models.Model):
    name1 = models.CharField(max_length=100,null=True,blank=True)
    img1 = models.ImageField(upload_to='media/')
    name2 = models.CharField(max_length=100,null=True,blank=True)
    img2 = models.ImageField(upload_to='media/')
    name3 = models.CharField(max_length=100,null=True,blank=True)
    img3 = models.ImageField(upload_to='media/')