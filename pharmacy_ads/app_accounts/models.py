from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLE_CHOICE=(
        ('owner','داروخانه دار'),
        ('pharmacist','داروساز'),
        ('admin','مدیر سایت'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICE,null=True,blank=True)


    def __str__(self):
        return f"{self.phone} ({self.get_role_display()})"

class OTP(models.Model):
    phone = models.CharField(max_length=11)
    code = models.CharField(max_length=6)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone} - {self.code}"
