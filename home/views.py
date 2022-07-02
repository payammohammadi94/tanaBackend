from itertools import product
from django.shortcuts import render,redirect
from .models import Category,Tablighat,Product,ImageGallery,Comment,VarientProduct
from django.contrib.auth.decorators import login_required
from .forms import CommentForm,ReplayForm
# Create your views here.


def home_show(request):
    category = Category.objects.filter(is_subcategory=False).order_by('-create')
    tablighat = Tablighat.objects.all()[0]
    context = {'category':category,'tablighat':tablighat}
    return render(request,'home/home.html',context)

        
#برای نمایش تمام محصولات   
def products_show(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'home/products.html',context)

# برای نمایش دسته بندی ها
def category_show(request,id):
    products_cats = Product.objects.filter(category=id)
    context = {'products_cats':products_cats}
    return render(request,'home/category.html',context)

#برای نمایش جزيیات محصولات
def detail_show(request,id):
    product = Product.objects.get(id=id)
    
    similar = product.tags.similar_objects()
    
    imageProduct = ImageGallery.objects.filter(product_id=id)
    
    commentForm = CommentForm()
    commentShow = Comment.objects.filter(product_id=id,is_replay=False).order_by('-id')
    
    replayForm = ReplayForm()
    liked = False
    if product.is_like.filter(username=request.user.username).exists():
        liked=True
        
    favorited = False
    if product.is_favorite.filter(username=request.user.username).exists():
        favorited=True
        
        
        
    if product.is_varient != None:
        varints =VarientProduct.objects.filter(product_id=id)
        print(varints)
        
        
    context = {'product':product,'imageProduct':imageProduct,'liked':liked,'favorited':favorited,'similar':similar,'commentForm':commentForm,'commentShow':commentShow,'replayForm':replayForm}
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
    
    
        
@login_required(login_url='/accounts/login/')
def comment_show(request,id):
    url = request.META.get('HTTP_REFERER')
    
    if request.method == 'POST':
        forms = CommentForm(request.POST)
        if forms.is_valid():
            data = forms.cleaned_data
            Comment.objects.create(product_id=id,user_id=request.user.id,comment=data['comment'],rate=data['rate'])
            return redirect(url)
        else:
            return redirect(url)
    else:
        return redirect(url)
    
@login_required(login_url='/accounts/login/') 
def likeComment_show(request,id):
    url = request.META.get('HTTP_REFERER')
    comment = Comment.objects.get(id=id)
    
    if comment.is_like.filter(username=request.user.username).exists():
        comment.is_like.remove(request.user)
        is_like_comment = False    
    else:
        comment.is_like.add(request.user)
        is_like_comment = True
    request.session['is_like_comment'] = is_like_comment
    return redirect(url)
        
        

@login_required(login_url='/accounts/login/')
def replayComment_show(request,id,comment_id):
    url = request.META.get('HTTP_REFERER')
    if request.method=='POST':
        form = ReplayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            Comment.objects.create(user_id=request.user.id,comment=data['comment'],product_id=id,is_replay=True,replay_id=comment_id)
            return redirect(url)
        else:
            return redirect(url)
    else:
        return redirect(url)