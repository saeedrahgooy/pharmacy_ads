from django.db import models

from app_accounts.models import UserProfile


class Ad(models.Model):
    ACTIVITY_CHOICES = (
        ('hospital','بیمارستانی'),
        ('city','شهری')
    )

    WORK_TIME_CHOICES = (
        ('daily','روزانه'),
        ('24h','شبانه روزی')
    )

    JOB_CHOICES = (
        ('investor', 'سرمایه‌گذار'),
        ('pharmacist_partner', 'داروساز مشارکت مدنی و همکاری'),
        ('pharmacist_responsible', 'داروساز مسئول فنی'),
        ('pharmacist_deputy', 'داروساز قائم مقام'),
        ('staff', 'پرسنل داروخانه'),
        ('technician', 'تکنسین دارویی'),
        ('cosmetics_seller', 'فروشنده آرایشی بهداشتی'),
        ('accountant', 'حسابدار'),
        ('intern', 'کارآموز'),
        ('other', 'سایر'),
    )
    COOP_CHOICES = (
        ('long', 'بلندمدت'),
        ('short', 'کوتاه‌مدت'),
        ('shift', 'شیفتی'),
    )

    EXP_CHOICES = (
        ('none', 'الزامی نیست'),
        ('1-3', '۱-۳ سال'),
        ('3+', '۳ سال به بالا'),
    )

    GENDER_CHOICES = (
        ('male', 'مرد'),
        ('female', 'زن'),
        ('any', 'فرقی ندارد'),
    )

    # ارتباط با داروخانه‌دار
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="ads")

    # فیلدهای آگهی
    title = models.CharField(max_length=200)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    work_time = models.CharField(max_length=20, choices=WORK_TIME_CHOICES)
    job_title = models.CharField(max_length=30, choices=JOB_CHOICES)
    cooperation_duration = models.CharField(max_length=20, choices=COOP_CHOICES)
    experience = models.CharField(max_length=20, choices=EXP_CHOICES)

    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50, blank=True, null=True)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="any")
    age_from = models.PositiveIntegerField(blank=True, null=True)
    age_to = models.PositiveIntegerField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=200, blank=True, null=True)
    special_conditions = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
