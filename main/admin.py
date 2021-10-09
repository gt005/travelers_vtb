from django.contrib import admin

from .models import DataUnit, Category


admin.site.register(Category)
admin.site.register(DataUnit)