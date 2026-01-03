from django.db import models
from app_accounts.models import UserProfile
from app_ads.models import Ad


class Request(models.Model):
    STATUS_CHOICES = (
        ('pending', 'در انتظار بررسی'),
        ('accepted', 'تایید شده'),
        ('rejected', 'رد شده'),
    )

    # داروساز درخواست می‌دهد
    pharmacist = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="pharmacist_requests"
    )

    # درخواست برای آگهی یک owner است
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name="ad_requests"
    )

    # صاحب آگهی (owner) برای راحتی دسترسی
    owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="owner_requests"
    )

    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"درخواست {self.pharmacist} برای {self.ad.title}"