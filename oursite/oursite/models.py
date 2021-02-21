from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, username_family, username_first, grade, department,email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
 
        user = self.model(
            username_family=username_family,
            username_first=username_first,
            grade=grade,
            department=department,
            email=email
        )
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, username_family, username_first, grade, department,email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username_family=username_family,
            username_first=username_first,
            grade=grade,
            department=department,
            email=email,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class StudentUser(AbstractBaseUser):
    username_family = models.CharField(max_length=255)
    username_first = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    email = models.CharField(
        verbose_name='メールアドレス',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
 
    objects = MyUserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username_family','username_first','grade','department']
 
    def __str__(self):
        return self.username_family
 
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