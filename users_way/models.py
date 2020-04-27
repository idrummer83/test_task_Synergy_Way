from django.db import models
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin


class SynergyGroup(models.Model):
    title = models.CharField(max_length=50, verbose_name='Group name')
    description = models.TextField(max_length=512, verbose_name='Group description')

    def __str__(self):
        return self.title


class SynergyUser(AbstractUser):
    first_name = models.CharField(max_length=15, verbose_name='first name')
    synergy_group = models.ForeignKey(SynergyGroup, on_delete=models.CASCADE, blank=True, null=True, verbose_name='user_group')

    def __str__(self):
        return self.username
