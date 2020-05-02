from django.contrib import admin
from . import models


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# Register your models here.
admin.site.register(models.Todo, TodoAdmin)

