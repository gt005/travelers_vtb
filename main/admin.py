from django.contrib import admin

from .models import DataUnit, Category, BaseUser


admin.site.register(Category)
admin.site.register(BaseUser)
admin.site.register(DataUnit)