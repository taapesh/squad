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


class SquadInvite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invited_by = models.CharField(max_length=255, blank=True)
    squad = models.ForeignKey("Squad", related_name="invites")
    user = models.ForeignKey("SquadUser", related_name="invites")
    created = models.DateTimeField(auto_now_add=True)

    def to_json(self):
        return {
            "created": self.created,
            "size": self.squad.size,
            "invited_by": self.invited_by
        }


class SquadActivity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    squad = models.ForeignKey("Squad", related_name="activity")
    user = models.ForeignKey("SquadUser", related_name="activity")
    text = models.CharField(max_length=255, blank=True)


class Pin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("SquadUser", related_name="pins", null=False)
    squad = models.ForeignKey("Squad", related_name="pins", null=False)
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lon = models.DecimalField(max_digits=11, decimal_places=8)
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    content_type = models.CharField(max_length=255, blank=True, null=True, default="none")
    content_url = models.CharField(max_length=255, blank=True, null=True)

    def to_json(self):
        return {
            "id": self.id,
            "lat": self.lat,
            "lon": self.lon,
            "title": self.title,
            "desc": self.description,
            "created_by": self.created_by,
            "created": self.created,
            "content_type": self.content_type,
            "content_url": self.content_url
        }


class FriendRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("SquadUser", related_name="friend_requests", null=False)
    requested_by = models.ForeignKey("SquadUser", null=False)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.user.username,
            "requested_by": self.requested_by.username,
            "requested_by_id": self.requested_by.id
        }


class Squad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    leader = models.OneToOneField("SquadUser", related_name="meta", null=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    size = models.IntegerField(null=False, default=1)
    created = models.DateTimeField(auto_now_add=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "desc": self.description,
            "created": self.created,
            "size": self.size,
            "leader": self.leader.username
        }


class SquadUserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
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
    avatar = models.CharField(max_length=255, blank=True, null=True)
    squad = models.ForeignKey("Squad", related_name="members", null=True)
    status = models.CharField(max_length=255, blank=True)
    friends = models.ManyToManyField("self")
    username = models.CharField(max_length=255, blank=False)
    token = models.CharField(max_length=255, blank=True)

    objects = SquadUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    def to_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
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
