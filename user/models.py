from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now= True, auto_now_add= False)
    image = models.ImageField(upload_to='image', blank=True, null=True)
    
    
    def __str__(self):
        return self.first_name
    
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'
        # abstract = False