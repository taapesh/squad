from __future__ import unicode_literals

from django.db import models

from decimal import Decimal
import uuid

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Promotion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    squad_size = models.IntegerField(null=True)


class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=255, blank=True)
    pin = models.ForeignKey("Pin", related_name="content")
    content_type = models.CharField(max_length=255, blank=False, null=False)


class Pin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("SquadUser", related_name="pins")
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lon = models.DecimalField(max_digits=11, decimal_places=8)
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Squad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    leader = models.OneToOneField("SquadUser", related_name="meta")
    size = models.IntegerField(null=False, default=1)
    created = models.DateTimeField(auto_now_add=True)


class SquadUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class SquadUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    avatar = models.CharField(max_length=255, blank=True)
    squad = models.ForeignKey("Squad", related_name="members", null=True)
    status = models.CharField(max_length=255, blank=True)
    friends = models.ManyToManyField("self")
    token = models.CharField(max_length=255, blank=True)

    objects = SquadUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    def to_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "token": self.token
        }

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
        
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


