from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
import uuid


class MyUserManager(BaseUserManager):
    def create_user(self, surname, last_name, phone_number, email, language, currency, password=None):
        """
        Creates and saves a User with the given email, username and password.
        """
        

        if not surname:
            raise ValueError('Must have an Surname')

        if not last_name:
            raise ValueError('Must have an Last Name')   

        if not phone_number:
            raise ValueError('Must have an Phone Number')

        if not email:
            raise ValueError('Must have an email address')
             
        if not language:
            raise ValueError('Must have an Language')

        if not currency:
            raise ValueError('Must have Currency')

        user = self.model(
            email=self.normalize_email(email),
            surname=surname,
            last_name=last_name,
            phone_number = phone_number,
            language = language,
            currency = currency,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, surname, last_name, phone_number, email , language, currency, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            surname=surname,
            last_name=last_name,
            phone_number = phone_number,
            language = language,
            currency = currency,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    surname = models.CharField(max_length = 100, unique=True)
    last_name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 20)
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=20) 
    tk = models.CharField(default=uuid.uuid4(), unique=True, max_length=255, primary_key=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['surname','last_name','phone_number','language','currency',]

    def __str__(self):
        return self.email

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