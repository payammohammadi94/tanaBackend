from django import forms
from .models import Profile
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    last_name = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    user_name = forms.CharField(max_length=20)
    password_1 = forms.CharField(max_length=20)
    password_2 = forms.CharField(max_length=20)
    referer = forms.CharField(max_length=15,required=False)
    
    #validation_form
    def clean_user_name(self):
        
        username = self.cleaned_data['user_name']
        if User.objects.filter(username=username).exists():
            
            raise forms.ValidationError('قبلا این نام کاربری ثبت نام کرده است.')
        else:
            return username
        
    def clean_password_2(self):
        
        password1=self.cleaned_data['password_1']
        password2=self.cleaned_data['password_2']
        
        if password1!=password2:
            raise forms.ValidationError('رمزعبورهای وارد شده مانند هم نیستند.')
        return password1

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    
    
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['phone','address']
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email']
