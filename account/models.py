from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='آدرس ایمیل',
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    full_name = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    phone = models.CharField(max_length=12, unique=True, verbose_name='شماره موبایل')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Otp(models.Model):
    """
    Model for activating new User accounts with phone number
    by sending activation code
    """
    phone = models.CharField(max_length=11)
    code = models.SmallIntegerField()
    expiration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone