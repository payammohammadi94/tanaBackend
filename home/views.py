from django.shortcuts import render,redirect
from .models import Category,Tablighat,Product,ImageGallery
from django.contrib.auth.decorators import login_required
# Create your views here.


def home_show(request):
    category = Category.objects.filter(is_subcategory=False).order_by('-create')
    tablighat = Tablighat.objects.all()[0]
    context = {'category':category,'tablighat':tablighat}
    return render(request,'home/home.html',context)

        
    
def products_show(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'home/products.html',context)

def category_show(request,id):
    products_cats = Product.objects.filter(category=id)
    context = {'products_cats':products_cats}
    return render(request,'home/category.html',context)


def detail_show(request,id):
    product = Product.objects.get(id=id)
    imageProduct = ImageGallery.objects.filter(product_id=id)
    
    liked = False
    if product.is_like.filter(username=request.user.username).exists():
        liked=True
        
    favorited = False
    if product.is_favorite.filter(username=request.user.username).exists():
        favorited=True
        
    context = {'product':product,'imageProduct':imageProduct,'liked':liked,'favorited':favorited}
    return render(request,'home/details.html',context)
        
@login_required(login_url='/accounts/login/')
def like_show(request,id):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=id)
    if product.is_like.filter(username=request.user.username).exists():
        product.is_like.remove(request.user)
    else:
        product.is_like.add(request.user)

    return redirect(url)


@login_required(login_url='/accounts/login/')
def favorite_show(request,id):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=id)
    if product.is_favorite.filter(username=request.user.username).exists():
        product.is_favorite.remove(request.user)
    else:
        product.is_favorite.add(request.user)

    return redirect(url)
    
        