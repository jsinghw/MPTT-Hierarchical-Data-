from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from app.models import FileSystem

# Register your models here.
admin.site.register(FileSystem, DraggableMPTTAdmin)
