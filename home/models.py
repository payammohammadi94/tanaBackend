from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='sub_cat')
    is_subcategory = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='category',null=True,blank=True)
    color = models.CharField(max_length=25,blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    
    #برای نمایش تبلیغات 
class Tablighat(models.Model):
    name = models.CharField(max_length=15)
    information = RichTextField(blank=True,null=True)
    poster = models.ImageField(upload_to = 'tablighat')
    create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    

    
class Product(models.Model):
    
    VARIENT = (
        (None,'None'),
        ('size','سایز'),
        ('color','رنگ'),
    )
    #نوع دسته بندی
    category = models.ManyToManyField(Category, related_name='productCategoryRel',verbose_name='دسته‌بندی محصول')
     #نام محصول
    name = models.CharField(max_length=50,verbose_name='نام محصول')
    #اسلاگ برای دسترسی به محصولات
    slug = models.CharField(max_length=50,unique=True)
    #برند
    brand = models.ForeignKey('Brand', related_name='brand', on_delete=models.CASCADE,verbose_name='برند')
    #تعداد موجودی محصول
    amount = models.IntegerField(default = 0,verbose_name='تعداد موجودی محصول')
    #قیمت اولیه
    unit_price = models.BigIntegerField(verbose_name='قیمت محصول')
    #قیمت نهایی بعد از تخفیف
    total_price = models.BigIntegerField()
    #تخفیف
    discount = models.IntegerField(verbose_name='تخفیف',blank=True,null=True)
    #اطلاعات محصول
    information = RichTextField(blank=True,null=True)
    #زمان اینجاد محصول
    create = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    #زمان آپدیت محصول
    update = models.DateTimeField(auto_now=True,verbose_name='تاریخ به روز رسانی')
    #عکس محصولات
    image = models.ImageField(upload_to = 'products',verbose_name='عکس محصول')
    #آیا محصول فروش رفته یا نه؟
    sale = models.BooleanField(default=False,verbose_name='فروخته شده است؟')
    #برای چک کردن که آیا این محصول تنوع رنگ و سایز دارد؟
    is_varient = models.CharField(max_length=10,choices=VARIENT,blank=True,null=True)
    
    #وقتی کاربر لایک میکند ما میتوانیم آن را ثبت کنیم
    is_like = models.ManyToManyField(User,blank=True,related_name='like')
    total_like = models.IntegerField(default=0)
    
    # وقتی کاربر یک محصول را به عنوان مورد علاقه انتخاب میکند آن را ثبت میکنیم
    is_favorite = models.ManyToManyField(User,blank=True,related_name='favorite')
    total_favorite = models.IntegerField(default=0)
    
    #تعداد بازدید از محصول
    total_view = models.IntegerField(default=1)
    #برای نمایش محصولات مشابه
    tags = TaggableManager(blank=True)
    
    @property
    def total_price(self):
        if self.discount:
            price = (self.discount * self.unit_price)/100
            return int(self.unit_price - price)
        else:
            return self.unit_price
        
    def total_favorite(self):
        return self.is_favorite.count()
    
    def total_like(self):
        return self.is_like.count()
            
    
    def __str__(self):
        return self.name
    


# مدل برای برند
class Brand(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self) :
        return self.name
#مدل برای سایز بندی
class Size(models.Model):
    size = models.CharField(max_length=10,verbose_name='سایز')
    
    def __str__(self):
        return self.size

#مدل برای رنگ بندی
class Color(models.Model):
    color = models.CharField(max_length=20,verbose_name='رنگ')
    code_color = models.CharField(max_length=40,verbose_name='کد رنگ را وارد کنید.')
    
    def __str__(self):
        return self.color
    

class VarientProduct(models.Model):
    name = models.CharField(max_length=50,verbose_name='نام محصول')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='varient')
    color = models.ForeignKey(Color,on_delete=models.CASCADE,blank=True,null=True)
    size = models.ForeignKey(Size,on_delete=models.CASCADE,blank=True,null=True)
    #قیمت اولیه
    unit_price = models.BigIntegerField(verbose_name='قیمت محصول')
    #قیمت نهایی بعد از تخفیف
    total_price = models.BigIntegerField()
    #تخفیف
    discount = models.IntegerField(verbose_name='تخفیف',blank=True,null=True)
    #تعداد
    amount = models.IntegerField(default = 0,verbose_name='تعداد موجودی محصول',blank=True,null=True)
    #زمان آپدیت محصول
    update = models.DateTimeField(auto_now=True,verbose_name='تاریخ به روز رسانی')
    #عکس محصولات
    image = models.ImageField(upload_to = 'products',verbose_name='عکس محصول')
    #آیا محصول فروش رفته یا نه؟
    sale = models.BooleanField(default=False,verbose_name='فروخته شده است؟')
    
    
    @property
    def total_price(self):
        if self.discount:
            price = (self.discount * self.unit_price)/100
            return int(self.unit_price - price)
        else:
            return self.uni_price
            
    
    def __str__(self):
        return self.name



#برای گالری عکس
class ImageGallery(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'gallery')
    
    def __str__(self):
        return self.product.name
    
#مدل برای کامنت و رای
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    comment = models.TextField(blank=True,null=True)
    rate = models.IntegerField(default=1,blank=True,null=True)
    is_replay = models.BooleanField(default=False)
    replay = models.ForeignKey('self',on_delete=models.CASCADE,related_name='replya_rel',blank=True,null=True)
    create = models.DateTimeField(auto_now_add=True)
    
        #وقتی کاربر لایک میکند ما میتوانیم آن را ثبت کنیم
    is_like = models.ManyToManyField(User,blank=True,related_name='likeComment')
    total_like = models.IntegerField(default=0,blank=True,null=True)
    
    def __str__(self):
        return self.product.name
    
    def total_like(self):
        return self.is_like.count()
    

    
# مدل برای شلوار
# class CategoryPants(models.Model):
#     name = models.CharField(max_length=50,verbose_name='دسته بندی')
#     is_sub_cat = models.BooleanField(default=False,blank=True,null=True)
#     sub_category = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='sub_cat')