from django.db import models


from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

class User(AbstractBaseUser):
    """
    Custom user class.
    """
    email = models.EmailField('email address', unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perms(self, perm, obj=None):
        return self.is_admin

    USERNAME_FIELD ='email'

    def __unicode__(self):
        return self.email

class User_new(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=10)

    age = models.CharField(max_length=50)
    country = models.CharField(max_length=30)


    def __str__(self):
        return self.user_name


