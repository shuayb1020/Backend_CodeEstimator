from django.db import models
from user.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250, blank= False, null=False)
    desc = models.TextField()
    file1 = models.FileField(upload_to= 'code-file', blank=False, null=False)
    file2 = models.FileField(upload_to= 'code-file', blank=False, null=False)
    owned_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True ,null=True)
    winner = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.title
    
