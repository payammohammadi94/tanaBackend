from django.urls import path
from . import views

app_name='accounts'


urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_show,name='login'),
    path('logout/',views.logout_show,name='logout'),
    path('profile/',views.profile_show,name='profile'),
    path('edite-profile/',views.edite_profile_show,name='edite_profile'),

]
