from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Posts(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Posts'
    
class Candidate(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="candidates",blank=True,null=True)
    manifesto=models.TextField(blank=True,null=True)
    background_info=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.user.id_no} : {self.post}"