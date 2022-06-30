from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('',views.home_show,name='home_show'),
    path('products/',views.products_show,name='products_show'),
    path('categorys/<int:id>/',views.category_show,name='category_show'),
    path('detail/<int:id>/',views.detail_show,name='detail_show'),
    path('like/<int:id>/',views.like_show,name='like_show'),
    path('favorite/<int:id>/',views.favorite_show,name='favorite_show'),
]
