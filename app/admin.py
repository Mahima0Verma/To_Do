from django.contrib import admin

# Registering the model

from .models import Task

admin.site.register(Task)
