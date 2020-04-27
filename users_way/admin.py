from django.contrib import admin
from .models import SynergyGroup, SynergyUser


@admin.register(SynergyUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(SynergyGroup)
class GroupAdmin(admin.ModelAdmin):
    pass