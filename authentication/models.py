from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, id_no, gender, password=None):
        if not id_no:
            raise ValueError('Users must have an ID number')
        if not gender:
            raise ValueError('Users must have a gender')

        user = self.model(
            id_no=id_no,
            gender=gender,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id_no, gender, password):
        user = self.create_user(
            id_no=id_no,
            gender=gender,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    id_no = models.CharField(max_length=8, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_active = models.BooleanField(default=True)

    username = None  # Remove username field

    objects = CustomUserManager()

    USERNAME_FIELD = 'id_no'  # Set id_no as the username field
    REQUIRED_FIELDS = ['gender']

    class Meta:
        verbose_name_plural = "Users"
