from multiprocessing import context
import profile
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,ProfileUpdateForm,UserUpdateForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['user_name'],first_name=data['first_name'],last_name=data['last_name'],password=data['password_2'])
            user.save()
            messages.success(request, 'ثبت نام با موفقیت انجام شد.')
           #این قسمت برای بحث کد معرف می‌باشد.
            if data['referer']:
                profile_ref = Profile.objects.filter(referer=data['referer'])
                if profile_ref.exists():
                    profile_ref[0].user_use_referer.add(user)
                    
            
            return redirect('accounts:login')
        else:
            return redirect('accounts:register')
    else:
        form = RegisterForm()
        
    context = {'form':form}
    return render(request,'accounts/register.html',context)


#login
def login_show(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            
            if user is not None:
                login(request,user)
                messages.success(request, 'ورود با موفقیت انجام شد.')
                return redirect('home:home_show')
            
            else:
                return redirect('accounts:register')

    else:
        form = LoginForm()
    
    context = {"form":form}
    return render(request,'accounts/login.html',context)

@login_required(login_url='/accounts/login/')
def logout_show(request):
    logout(request)
    messages.success(request, 'شما از سایت خارج شدید.')
    return redirect('home:home_show')


@login_required(login_url='/accounts/login/')
def profile_show(request):
    profile = Profile.objects.get(user_id=request.user.id)
    number_of_referer = len(profile.user_use_referer.all())
    context={
        'profile':profile,
        'number_of_referer':number_of_referer
    }
    
    return render(request,'accounts/profile.html',context)



@login_required(login_url='/accounts/login/')
def edite_profile_show(request):
    if request.method=='POST':
        profileForm=ProfileUpdateForm(request.POST,instance=request.user.profile)
        userForm=UserUpdateForm(request.POST,instance=request.user)
        
        if profileForm.is_valid() and userForm.is_valid():
            profileForm.save()
            userForm.save()
            return redirect('accounts:profile')
        else:
            messages.error(request,'اطلاعاتی که وارد کردید فرمت درستی ندارد.')
            return redirect('accounts:profile')
    else:
        profileForm=ProfileUpdateForm(instance=request.user.profile)
        userForm=UserUpdateForm(instance=request.user)
        
    context={
        
        "profileForm":profileForm,
        "userForm":userForm
    }
    
    return render(request,'accounts/editProfile.html',context)
        
            
    