from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin, 
                                        BaseUserManager)
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', unique=True)
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    phone = models.CharField('Phone', max_length=30, blank=True)
    #company = models.ForeignKey(Company,
    #                            on_delete=models.CASCADE,
    #                            null=True,
    #                            blank=True)
    is_staff = models.BooleanField('Is Staff', default=False, help_text='If user is staff') # NoQa
    is_active = models.BooleanField('Is Active', default=False, help_text='Is user is active') # NoQa
    date_joined = models.DateTimeField('Date Joined', default=timezone.now)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Users'
        ordering = ['date_joined']

    def __str__(self):
        return self.email
