from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
        related_query_name="user",
    )


class TrainerProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="trainer_profile"
    )
    bio = models.TextField(blank=True)
    specialization = models.CharField(max_length=255)
    experience = models.PositiveIntegerField(blank=True, null=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username
