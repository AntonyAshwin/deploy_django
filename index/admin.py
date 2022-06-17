from django.contrib import admin
from .models import FormModel

# Register your models here.

class RegisterContent(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(FormModel, RegisterContent)
