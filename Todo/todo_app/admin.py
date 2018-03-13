from django.contrib import admin
from .models import Todo

@admin.register(Todo) # Register your models to the admin console
class TodoAdmin(admin.ModelAdmin):
    list_display = ('text', 'complete') # Beautify the Admin Interface
