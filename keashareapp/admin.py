from django.contrib import admin
from . import models

admin.site.register(models.AppGroup)
admin.site.register(models.Post)