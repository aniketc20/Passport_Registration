from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here. A CUSTOM USER MODEL HAS BEEN CREATED WITH LOGIN CREDENTIALS AS PHONE NUMBER AND PASSWORD
class MyAccountManager(BaseUserManager):
    def create_user(self, phone_number, full_name, d_o_b, email, passport_number, image, password=None):
        if not phone_number:
            raise ValueError('Users must have an email address')
        if not full_name:
            raise ValueError('Users must have a fullname')
        if not email:
            raise ValueError('Users must have a email')
        if not d_o_b:
            raise ValueError('Users must have a d_o_b')
        if not passport_number:
            raise ValueError('Users must have a passport')
        if not image:
            raise ValueError('Users must have an Image')

        user = self.model(
            phone_number=phone_number,
            full_name=full_name,
            d_o_b=d_o_b,
            email=self.normalize_email(email),
            passport_number=passport_number,
            image=image
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, full_name, d_o_b, email, passport_number, password):
        user = self.create_user(
            phone_number=phone_number,
            full_name=full_name,
            d_o_b=d_o_b,
            email=self.normalize_email(email),
            passport_number=passport_number,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    username = None  # removes username field
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    full_name = models.CharField(max_length=30, unique=False)
    d_o_b = models.DateField(verbose_name='date of birth')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now=True)
    phone_number = models.IntegerField(verbose_name='ph_no', unique=True)
    passport_number = models.IntegerField(verbose_name='passport_no', unique=True)
    image = models.ImageField(upload_to='profile_image', blank=False)  # uploads pics to a folder called "profile_image"

    USERNAME_FIELD = 'phone_number'  # this tells django to use phone_number instead of username
    REQUIRED_FIELDS = ['full_name',  # all the required fields during user registration
                       'd_o_b',
                       'email',
                       'passport_number',
                       'image'
                       ]
    objects = MyAccountManager()

    def __str__(self):
        return str(self.phone_number)  # converts to string for displaying in database

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
