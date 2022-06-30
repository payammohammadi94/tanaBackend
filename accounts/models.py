from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import random
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15,blank=True,null=True)
    address = models.CharField(max_length=500)
    referer = models.CharField(max_length=6,blank=True,null=True)
    user_use_referer = models.ManyToManyField(User,blank=True,related_name='user_referer')
    
    def __str__(self) -> str:
        return self.user.username
    
    
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    random_referer = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    if created:
        referer = ''.join(random.sample(random_referer,5))
        Profile.objects.create(user=instance,referer=referer)
        
        
        
    
    