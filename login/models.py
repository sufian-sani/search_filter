from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    # image=models.ImageField(default='default.jpg', upload_to='session/images')
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=150,blank=True)
    biodata=models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
