from django.contrib import admin

# Register your models here.
from .models import Location, Category

admin.site.register(Location)
admin.site.register(Category)