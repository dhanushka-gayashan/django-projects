from django.contrib import admin
from . import models


# Register your models here.
# Group Members can be edited inside of the Group Interface on Admin Page
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
