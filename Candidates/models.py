from django.db import models
from django.contrib.auth.models import User#username,email, first_name,last_name,is_active,is_superuser


# Create your models here.
#types of relationships
## 1. One To One - user and candidate/voter -OneToOneField
## 2. One To Many - post and candidates -ForeignKey
## 3. Many To Many - votes to candidates - ManyToManyField

class Posts(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Candidate(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="candidates",blank=True,null=True)
    id_no=models.CharField(max_length=8)
    manifesto=models.TextField(blank=True,null=True)
    background_info=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.id_no} : {self.user.username}"