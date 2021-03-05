from djongo import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Songs(models.Model):
    songid = models.CharField(max_length=200)
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    userid = models.CharField(max_length=12, primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    joindate = models.CharField(max_length=25)
    sang_songs = models.ArrayField(
        model_container=Songs
    )
    re_songs = models.ArrayField(
        model_container=Songs
    )
    pi_re_songs = models.ArrayField(
        model_container=Songs
    )
    pitch = models.FloatField(default=0.0)
    objects = UserManager()

    REQUIRED_FIELDS = ['joindate']
    USERNAME_FIELD = 'userid'

class WavFile(models.Model):
    file = models.FileField()
    class Meta:
        managed = False